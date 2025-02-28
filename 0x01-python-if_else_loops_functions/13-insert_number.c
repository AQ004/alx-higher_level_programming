#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function that inserts a number into a
 *               sorted singly linked list.
 * @head: pointer to pointer to the head of the list
 * @number: the number
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *temp;

	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}

	temp = *head;

	while (temp->next != NULL && number > (temp->next)->n)
		temp = temp->next;
	new->next = temp->next;
	temp->next = new;

	return (new);
}
