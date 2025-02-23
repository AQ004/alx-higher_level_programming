#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - a function returns an integer
 * @list: pointer to a list
 * Description: this function is to determine if there
 *               is a cycle or not by a famous method
 * Return: one if there is a cycle in the linked list, zero otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (fast == slow)
			return (1);
	}

	return (0);
}

