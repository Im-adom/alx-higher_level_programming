#include <Python.h>
#include <object.h>
#include <listobject.h>
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int g;

	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (g = 0; g < size; g++)
	printf("Element %g: %s\n", g, Py_Type(obj->ob_item[g]->tp_name);
}
