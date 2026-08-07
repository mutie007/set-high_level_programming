#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to head of list
 * Return: pointer to new head
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (head != NULL)
	{
		next = head->next;
		head->next = prev;
		prev = head;
		head = next;
	}
	return (prev);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *second_half, *tmp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	slow = *head;
	fast = *head;

	/* Find the middle (slow will point to middle) */
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/* Reverse the second half */
	second_half = reverse_list(slow);
	tmp = second_half;

	/* Compare first half and reversed second half */
	while (tmp != NULL)
	{
		if ((*head)->n != tmp->n)
		{
			/* Restore the list before returning */
			reverse_list(second_half);
			return (0);
		}
		*head = (*head)->next;
		tmp = tmp->next;
	}

	/* Restore the list */
	reverse_list(second_half);
	return (1);
}
