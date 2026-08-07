#include "lists.h"

/**
 * reverse - reverses a linked list
 * @head: pointer to the head
 * Return: pointer to the new head
 */
listint_t *reverse(listint_t *head)
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
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *rev, *tmp;

	if (!*head || !(*head)->next)
		return (1);

	/* Find middle */
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/* Reverse second half */
	rev = reverse(slow);

	/* Compare */
	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}

	return (1);
}
