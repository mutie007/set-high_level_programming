#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 * Return: pointer to the new head
 */
static listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (head)
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
 * @head: double pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *second_half, *first_half;

	if (!head || !*head || !(*head)->next)
		return (1);

	/* Find middle using slow/fast pointers */
	slow = *head;
	fast = *head;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/* Reverse second half */
	second_half = reverse_list(slow);
	first_half = *head;

	/* Compare the two halves */
	while (second_half)
	{
		if (first_half->n != second_half->n)
		{
			/* Restore list before returning failure */
			reverse_list(second_half);
			return (0);
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}

	/* Restore the original list */
	reverse_list(slow);
	return (1);
}
