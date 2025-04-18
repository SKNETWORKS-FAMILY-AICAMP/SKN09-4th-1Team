from django import forms
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = [
            'marital_skipped', 'marital_status', 'marriage_duration', 'divorce_status',
            'children_skipped', 'has_children', 'children_ages',
            'other_skipped', 'property_range', 'experience',
            'detail_skipped', 'detail_info'
        ]

    def clean(self):
        cleaned_data = super().clean()

        # ✅ 혼인 정보 유효성
        if not cleaned_data.get('marital_skipped'):
            if not cleaned_data.get('marital_status'):
                self.add_error('marital_status', '혼인 상태를 입력해주세요.')
            if not cleaned_data.get('marriage_duration'):
                self.add_error('marriage_duration', '혼인 기간을 입력해주세요.')
            if not cleaned_data.get('divorce_status'):
                self.add_error('divorce_status', '이혼 상태를 선택해주세요.')

        # ✅ 자녀 정보 유효성
        if not cleaned_data.get('children_skipped'):
            if cleaned_data.get('has_children') is None:
                self.add_error('has_children', '자녀 유무를 선택해주세요.')
            elif cleaned_data.get('has_children') and not cleaned_data.get('children_ages'):
                self.add_error('children_ages', '자녀 나이를 입력해주세요.')

        # ✅ 기타 정보 유효성
        if not cleaned_data.get('other_skipped'):
            if not cleaned_data.get('property_range'):
                self.add_error('property_range', '재산 범위를 선택해주세요.')
            if not cleaned_data.get('experience'):
                self.add_error('experience', '경험 여부를 선택해주세요.')

        # ✅ 고민 정보 유효성
        if not cleaned_data.get('detail_skipped') and not cleaned_data.get('detail_info'):
            self.add_error('detail_info', '상세 고민을 입력해주세요.')

        return cleaned_data
