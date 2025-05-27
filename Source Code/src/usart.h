#ifndef USART_H
#define USART_H

void usart_init(unsigned long baud);
void usart_send(char data);
void usart_print_number(uint16_t num);

#endif