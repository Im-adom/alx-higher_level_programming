#include "lists.h"
/**
 * reverse_listint - This function reverses a singly-linked list
 * @head: pointer to starting node
 * Return: pointer to the first node in new list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *init = NULL;

	while (node)
	{
		next = node->next;
		node->next = init;
		node = next;
	}
	*head = init;
	return (*head);
}
/**
 * is_palindrome - This function checks if a linked list is a
 * palindrome.
 * @head: pointer ti the head of the linked list.
 * Return: 0 if the list is not a palindrome, otherwise
 * return -1
 */
int is_palindrome(listint_t **head)
{
	listint *ptr_rev, *temp, *gee;
	size_t size = 0, a;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}
	temp = *head;
	for (a = 0; a < (size / 2) - 1; a++)
		temp = temp->next;
	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);
	temp = temp->next->next;
	ptr_rev = reverse_listint(&temp);
	gee = ptr_rev;

	temp = *head;
	while (ptr_rev)
	{
		if (temp->n != ptr_rev->n)
			return (0);
		temp = temp->next;
		ptr_rev = ptr_rev->next;
	}
	reverse_listint(&gee);

	return (1);
}
