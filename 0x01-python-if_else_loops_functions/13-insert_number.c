#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - insert a node in sorted linked list.
 * @head: head of the list.
 * @number: data of newnode.
 * Return: position of newnode.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *tmp;

	if (head == NULL)
		return (NULL);
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	if (*head == NULL)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	tmp = *head;
	if (number < tmp->n)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	while (tmp->next)
	{
		if (tmp->next->n <= number)
		{
			tmp = tmp->next;
		}
		else
		{
			break;
		}
	}
	if (tmp->next == NULL)
	{
		newnode->next = NULL;
		tmp->next = newnode;
	}
	else
	{
		newnode->next = tmp->next;
		tmp->next = newnode;
	}
	return (newnode);
}
