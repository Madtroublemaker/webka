from rest_framework import serializers

from .models import Company, Vacancy

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'city', 'address']

# class VacancySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     description = serializers.CharField()
#     salary = serializers.FloatField()
#     company_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

#     def create(self, validated_data):
#         return Vacancy.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.salary = validated_data.get('salary', instance.salary)
#         instance.company_id = validated_data.get('company_id', instance.company_id)
#         instance.save()
#         return instance
class VacancySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    salary = serializers.FloatField()
    company_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    def create(self, validated_data):
        company_id = validated_data.pop('company_id').id
        vacancy = Vacancy.objects.create(company_id=company_id, **validated_data)
        return vacancy

    def update(self, instance, validated_data):
        company_id = validated_data.pop('company_id').id
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.company_id = company_id
        instance.save()
        return instance
