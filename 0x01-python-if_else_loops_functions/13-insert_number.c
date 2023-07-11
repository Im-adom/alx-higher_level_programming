#include "lists.h"
/**
 * insert_node - inserts a number into sorted linked list.
 * @head: the head of the list
 * @number: the number to store in the new node
 * Return: the pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr;
	listint_t *n;

	ptr = *head;

	n = malloc(sizeof(lsitint_t));
	if (n == NULL)
		return (NULL);
	n->node = number;

	if (*head == NULL || (*head)->node > number)
	{
		n->next = *head;
		*head = n;
		return (n);
	}
	while (ptr->next != NULL)
	{
		if ((ptr->next)->node >= number)
		{
			n->next = ptr->next;
			ptr->next = n;
			return (n);
		}
		ptr = ptr->next;
	}
	n->next = NULL;
	ptr->next = n;
	return (n);
}
