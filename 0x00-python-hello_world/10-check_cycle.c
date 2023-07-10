#include "lists.h"
/**
 * check_cycle - checks if a linked list has a cycle in it.
 * @list: linked list to check
 * Return: 1 if there is a cycle and 0 if there is none
 */
int check_cycle(listint_t *list)
{
	listint_t *cyc, *check;

	if  (list == NULL || list->next == NULL)
		return (0);
	cyc = list;
	check = cyc->next;

	while (cyc != NULL && check->next!= NULL && check->next->next != NULL)
	{
		if (cyc == check)
			return (1);
		cyc = cyc->next;
		check = check->next->next;
	}
	return (0);
}
