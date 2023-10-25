from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):

  class Meta:
    model = Item
    fields = ['id','description','created_at','updated_at']
    extra_kwargs = {'description':{
                      'allow_null':False,
                      'error_messages': {
                        'blank': 'Description is required.',
                        'null': 'Description is required.'
                      }
                    }
                  }