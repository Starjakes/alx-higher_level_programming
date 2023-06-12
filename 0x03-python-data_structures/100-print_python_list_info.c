#include  "Python.h"

void print_python_list_info(PyObject *p)
{
  PyListObject *list;
  Py_ssize_t size, a;
  PyObject *object;
  struct _typeobject *type;

  if (strcmp(p->ob_type->tp_name, "list") == 0)
    {
      list = (PyListObject *)p;
      size = list->ob_base.ob_size;
      printf("[*] Size of the Python List = %ld\n", size);
      printf("[*] Allocated = %ld\n", list->allocated);
      for (a = 0; a < size; a++)
	{
	  object = list->ob_item[a];
	  type = object->ob_type;
	  printf("Element %ld: %s\n", a, type->tp_name);
	}
    }
}
