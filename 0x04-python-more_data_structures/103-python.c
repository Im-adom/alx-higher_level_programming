#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes info.
 * @p: Python Object
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	char *ptr_str;
	long int size, g, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	ptr_str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", ptr_str);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (g = 0; g < limit; g++)
		if (ptr_str[g] >= 0)
			printf(" %02x", ptr_str[g]);
		else
			printf(" %02x", 256 + ptr_str[g]);

	printf("\n");
}

/**
 * print_python_list - This function prints list info.
 * @p: Python Object
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	long int size, g;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (g = 0; g < size; g++)
	{
		obj = ((PyListObject *)p)->ob_item[g];
		printf("Element %ld: %s\n", g, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
