from graphene_django.types import ObjectType
from graphene_django_extras import DjangoFilterPaginateListField

from apps.employees.schema import mutation
from apps.employees.schema import types

__all__ = [
    'EmployeeQuery', 'EmployeeMutation'
]


class EmployeeQuery(ObjectType):
    positions = DjangoFilterPaginateListField(types.PositionType)
    specializations = DjangoFilterPaginateListField(types.SpecializationType)
    employees = DjangoFilterPaginateListField(types.EmployeeType)

    class Meta:
        abstract = True


class EmployeeMutation(ObjectType):
    position_create = mutation.ModelPositionMutation.CreateField()
    position_update = mutation.ModelPositionMutation.UpdateField()
    position_delete = mutation.ModelPositionMutation.DeleteField()

    specialization_create = mutation.ModelSpecializationMutation.CreateField()
    specialization_update = mutation.ModelSpecializationMutation.UpdateField()
    specialization_delete = mutation.ModelSpecializationMutation.DeleteField()

    employee_create = mutation.ModelEmployeeMutation.CreateField()
    employee_update = mutation.ModelEmployeeMutation.UpdateField()
    employee_delete = mutation.ModelEmployeeMutation.DeleteField()

    class Meta:
        abstract = True
