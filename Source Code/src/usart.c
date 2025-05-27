#include <avr/io.h>
#include "usart.h"
#include <stdlib.h> // for itoa()

#define F_CPU 16000000UL

void usart_init(unsigned long baud) {
    uint16_t ubrr = (F_CPU / 16 / baud) - 1;
    UBRR0H = (ubrr >> 8);
    UBRR0L = ubrr;
    UCSR0B = (1 << TXEN0);
    UCSR0C = (1 << UCSZ01) | (1 << UCSZ00);
}

void usart_send(char data) {
    while (!(UCSR0A & (1 << UDRE0)));
    UDR0 = data;
}

void usart_print_number(uint16_t num) {
    char buffer[6];
    itoa(num, buffer, 10);
    for (char *p = buffer; *p; p++) {
        usart_send(*p);
    }
}