#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to the head of the list
 * @number: the number to insert
 *
 * Return: address of the new node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	/* Empty list or insert at the beginning */
	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	/* Find the correct position */
	current = *head;
	while (current->next != NULL && current->next->n < number)
		current = current->next;

	new->next = current->next;
	current->next = new;

	return (new);
}
