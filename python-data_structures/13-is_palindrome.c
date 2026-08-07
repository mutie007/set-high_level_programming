#include "lists.h"

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
	listint_t *slow, *fast, *rev_head, *tmp;
	int result = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	/* Find the middle of the list */
	slow = *head;
	fast = *head;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/* Reverse the second half */
	rev_head = reverse_list(slow);

	/* Compare first half with reversed second half */
	tmp = *head;
	while (rev_head != NULL)
	{
		if (tmp->n != rev_head->n)
		{
			result = 0;
			break;
		}
		tmp = tmp->next;
		rev_head = rev_head->next;
	}

	return (result);
}
