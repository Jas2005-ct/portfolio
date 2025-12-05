from rest_framework import serializers
from .models import CustomUser, Profile, Education, Certificate, Internship, Profession, Skill, Project, SocialLink, Resume, Service, Testimonial, ContactMessage, Technology



class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
        read_only_fields = ['user']

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'
        read_only_fields = ['user']

class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = '__all__'
        read_only_fields = ['user']

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'
        read_only_fields = ['user']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
        read_only_fields = ['user']

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    # tech_stack = serializers.SerializerMethodField() # Removed to allow legacy model field
    technologies = TechnologySerializer(many=True, read_only=True)
    technology_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Technology.objects.all(), source='technologies'
    )

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['user']

    # def get_tech_stack(self, obj):
    #     return ", ".join([tech.name for tech in obj.technologies.all()])

class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'
        read_only_fields = ['user']

class ResumeSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = Resume
        fields = ['id', 'user', 'resume', 'file_url']
        read_only_fields = ['user']

    def get_file_url(self, obj):
        return obj.resume.url

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = ['user']

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'
        read_only_fields = ['user']

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
        read_only_fields = ['user', 'created_at']



class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    technologies = TechnologySerializer(many=True, read_only=True)
    technology_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Technology.objects.all(), source='technologies'
    )

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['user']
