#include "lists.h"

/**
 * is_palindrome - checks if a list is palindrome
 * @head: list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    static listint_t *list;

    if (current == NULL)
        return (1);
    if (list == NULL)
        list = current;
    if (is_palindrome(&current->next) && list->n == current->n)
    {
        list = list->next;
        current = current->next;
        return (1);
    }
    list = current;
    return (0);   
}
