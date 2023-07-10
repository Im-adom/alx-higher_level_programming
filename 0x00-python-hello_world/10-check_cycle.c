#include "lists.h"
/**
 * check_cycle - checks if a linked list has a cycle in it.
 * @list: linked list to check
 * Return: 1 if there is a cycle and 0 if there is none
 */
int check_cycle(listint_t *list)
{
	listint_t *a = list;
	listint_t *b = list;

	if (!list)
		return (0);
	while (a && b && a->next)
	{
		a = a->next;
		b = b->next->next;
		if (a == b)
			return (1);
	}
	return (0);
}
