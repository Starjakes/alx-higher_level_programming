#include "lists.h"
/**
 * is_palindrome - function that check if a singly linked is palindrome
 * @head:list
 *Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	const listint_t *current;
	int len;
	int a, b;
	int arr[10000];

	if (*head == NULL)
		return (1);
	current = *head;
	len = 0;
	while (current != NULL)
	{
		current = current->next;
		len++;
	}
	if (len == 1)
		return (1);

	current = *head;
	a = 0;
	while (current != NULL)
	{
		arr[a] = current->n;
		a++;
		current = current->next;
	}
	b = 0;
	a--;
	len--;
	while (a >= (len / 2))
	{
		if (arr[a] != arr[b])
			return (0);
		a--;
		b++;
	}
	return (1);
}
