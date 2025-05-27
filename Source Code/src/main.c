#include <avr/io.h>
#include <util/delay.h>
#include "usart.h"
#include "spi.h"

#define F_CPU 16000000UL

#define SENSOR_PIN 0      // ADC0
#define PUMP_PIN   PD3    // Digital pin 3

// Wajah 8x8
uint8_t sadFace[8] = {
  0b10000001,
  0b01111110,
  0b00000000,
  0b00000000,
  0b00011000,
  0b00000000,
  0b10011001,
  0b01100110
};


uint8_t neutralFace[8] = {
  0b01111110,
  0b01111110,
  0b00000000,
  0b00111100,
  0b00000000,
  0b11100111,
  0b11100111,
  0b00000000
};


uint8_t happyFace[8] = {
  0b00111100,
  0b01000010,
  0b00000000,
  0b00011000,
  0b00011000,
  0b01000010,
  0b10100101,
  0b01000010
};


void initADC() {
    ADMUX  = (1 << REFS0); // AVcc reference
    ADCSRA = (1 << ADEN)  | (1 << ADPS2) | (1 << ADPS1); // Enable ADC, prescaler 64
}

uint16_t readADC(uint8_t ch) {
    ADMUX = (ADMUX & 0xF0) | (ch & 0x0F); // Select channel
    ADCSRA |= (1 << ADSC);               // Start conversion
    while (ADCSRA & (1 << ADSC));        // Wait to finish
    return ADC;
}

void sendCommand(uint8_t address, uint8_t data) {
    PORTB &= ~(1 << PB2); // CS LOW
    spi_send(address);
    spi_send(data);
    PORTB |= (1 << PB2);  // CS HIGH
}

void initMAX7219() {
    sendCommand(0x09, 0x00);
    sendCommand(0x0A, 0x08);
    sendCommand(0x0B, 0x07);
    sendCommand(0x0C, 0x01);
    sendCommand(0x0F, 0x00);
    for (uint8_t i = 1; i <= 8; i++) sendCommand(i, 0x00);
}

void showFace(uint8_t *face) {
    for (uint8_t i = 0; i < 8; i++) {
        sendCommand(i + 1, face[i]);
    }
}

int main(void) {
    DDRD |= (1 << PUMP_PIN);
    PORTD &= ~(1 << PUMP_PIN);
    
    usart_init(9600);
    spi_init();
    initADC();
    initMAX7219();

    while (1) {
        uint16_t moisture = readADC(SENSOR_PIN);
        uint8_t percent = 100 - ((moisture * 100UL) / 1023);
        usart_print_number(percent);
        usart_send('\n');

        if (percent <= 20) {
            PORTD |= (1 << PUMP_PIN);
            showFace(sadFace);
        } else if (percent <= 40) {
            PORTD &= ~(1 << PUMP_PIN);
            showFace(neutralFace);
        } else {
            PORTD &= ~(1 << PUMP_PIN);
            showFace(happyFace);
        }

        _delay_ms(1000);
    }
}