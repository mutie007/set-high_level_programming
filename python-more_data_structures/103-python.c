#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints basic info about a Python list object
 * @p: pointer to the PyObject representing the list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyListObject *list = (PyListObject *)p;
	PyObject *obj;

	size = list->ob_base.ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		obj = list->ob_item[i];
		printf("Element %ld: %s\n", i, obj->ob_type->tp_name);
		if (strcmp(obj->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(obj);
	}
}

/**
 * print_python_bytes - prints basic info about a Python bytes object
 * @p: pointer to the PyObject representing the bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i, limit;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");

	if (p == NULL || strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = bytes->ob_base.ob_size;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);

	limit = size + 1;
	if (limit > 10)
		limit = 10;

	printf("  first %ld bytes: ", limit);
	for (i = 0; i < limit; i++)
	{
		printf("%02x", bytes->ob_sval[i] & 0xff);
		if (i < limit - 1)
			printf(" ");
	}
	printf("\n");
}
