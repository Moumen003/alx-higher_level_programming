#include "lists.h"

listint_t *rev(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * rev - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *rev(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if palindrome.
 * @head: ptr linked list.
 *
 * Return:  0 succes.
 */
int is_palindrome(listint_t **head)
{
	listint_t *t, *malo, *middle;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	t = *head;
	while (t)
	{
		size++;
		t = t->next;
	}

	t = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		t = t->next;

	if ((size % 2) == 0 && t->n != t->next->n)
		return (0);

	t = t->next->next;
	malo = rev(&t);
	middle = malo;

	t = *head;
	while (malo)
	{
		if (t->n != malo->n)
			return (0);
		t = t->next;
		malo = malo->next;
	}
	rev(&middle);

	return (1);
}
