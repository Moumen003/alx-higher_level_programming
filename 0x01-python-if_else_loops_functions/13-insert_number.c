#include "lists.h"

/**
* insert_node - fn name
* @head: fen da
* @number: el makan
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!ptr || new->n < ptr->n)
	{
		new->next = ptr;
		return (*head = new);
	}

	while (ptr)
	{
		if (!ptr->next || new->n < ((ptr->next)->n))
		{
			new->next = ptr->next;
			ptr->next = new;
			return (ptr);
		}
		ptr = ptr->next;
	}
	return (NULL);
}
