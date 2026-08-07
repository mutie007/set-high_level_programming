#include "lists.h"

listint_t *reverse_list(listint_t *head);

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 * Return: pointer to the new head
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
 * @head: double pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *rev_head, *curr;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	/* Find middle */
	slow = *head;
	fast = *head;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/* Reverse second half */
	rev_head = reverse_list(slow);

	/* Compare */
	curr = *head;
	while (rev_head != NULL)
	{
		if (curr->n != rev_head->n)
			return (0);
		curr = curr->next;
		rev_head = rev_head->next;
	}

	return (1);
}
