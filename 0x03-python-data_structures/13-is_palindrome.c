#include "lists.h"
/**
 * is_palindrome - checks a singly linked list.
 * @head: a double pointer
 * Return: 1 if the list is a palindrome otherwise 0
 */
int is_palindrome(listint_t **head)
{
	return (head && is_pseudo_palindrome(head, *head));
}

/**
 * check_pseudo_palindrome - a function to help with the singly list
 * @head: pointer
 * @tail: pointer
 * Return:..
 */
int check_pseudo_palindrome(listint_t **head, listint_t *tail)
{
	int search = 1;

	if (tail)
	{
		search = is_pseudo_palindrome(head, tail->next);

		if (tail == *head || tail->next == *head)
			*head = tail;
		else if (search && (*head)->n == tail->n)
			*head = (*head)->next;
		else
			search = 0;
	}
	return (search);
}
