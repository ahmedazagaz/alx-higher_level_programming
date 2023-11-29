#include "lists.h"

/**
* insert_node -  inserts a number into a sorted singly linked list.
* @head: head node.
* @number: number to be inserted.
* Return: address of the new node or NULL if fails.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *previous;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}
	current = *head;
	while (current != NULL && current->n < number)
	{
		previous = current;
		current = current->next;
	}
	new->next = current;
	previous->next = new;
	return (new);
}
