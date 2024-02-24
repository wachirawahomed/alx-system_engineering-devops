#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - creates an infinite loop to make the program hang
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 * Return: 0
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			/* Sleep to avoid too fast creation of zombies */
			sleep(1);
		}
		else if (pid == 0)
		{
			/* Child exits immediately, becoming a zombie */
			exit(0);
		}
		else
		{
			perror("fork");
			return (1);
		}
	}

	infinite_while(); /* Infinite loop to keep the program running */
	return (0);
}
