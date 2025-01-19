import unittest
from unittest.mock import Mock, patch, MagicMock
import requests
from typing import Dict, Any

class ExternalService:
    def get_user_data(self, user_id: int) -> Dict[str, Any]:
        """외부 API에서 사용자 데이터를 가져오는 메서드"""
        response = requests.get(f"https://api.example.com/users/{user_id}")
        return response.json()

class UserService:
    def __init__(self, external_service: ExternalService):
        self.external_service = external_service
    
    def get_user_name(self, user_id: int) -> str:
        """사용자 ID로 이름을 조회하는 메서드"""
        try:
            user_data = self.external_service.get_user_data(user_id)
            return user_data['name']
        except Exception as e:
            raise ValueError(f"사용자 데이터를 가져올 수 없습니다: {str(e)}")
    
    def is_adult(self, user_id: int) -> bool:
        """사용자가 성인인지 확인하는 메서드"""
        user_data = self.external_service.get_user_data(user_id)
        return user_data.get('age', 0) >= 18

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.external_service_mock = Mock(spec=ExternalService)
        self.user_service = UserService(self.external_service_mock)
    
    def test_get_user_name_success(self):
        """사용자 이름 조회 성공 테스트"""
        # Mock 설정
        self.external_service_mock.get_user_data.return_value = {
            'id': 1,
            'name': '홍길동',
            'age': 30
        }
        
        # 테스트 실행
        name = self.user_service.get_user_name(1)
        
        # 검증
        self.assertEqual(name, '홍길동')
        self.external_service_mock.get_user_data.assert_called_once_with(1)
    
    def test_get_user_name_error(self):
        """사용자 이름 조회 실패 테스트"""
        # Mock이 예외를 발생시키도록 설정
        self.external_service_mock.get_user_data.side_effect = Exception("API 오류")
        
        # 예외 발생 검증
        with self.assertRaises(ValueError):
            self.user_service.get_user_name(1)
    
    def test_is_adult(self):
        """성인 확인 테스트"""
        # 테스트 케이스 설정
        test_cases = [
            ({'age': 20}, True),  # 성인
            ({'age': 15}, False), # 미성년자
            ({}, False),          # 나이 정보 없음
        ]
        
        for user_data, expected in test_cases:
            with self.subTest(user_data=user_data):
                self.external_service_mock.get_user_data.return_value = user_data
                result = self.user_service.is_adult(1)
                self.assertEqual(result, expected)

# patch 데코레이터를 사용한 테스트
class TestExternalService(unittest.TestCase):
    @patch('requests.get')
    def test_get_user_data(self, mock_get):
        """외부 API 호출 테스트"""
        # Mock 응답 설정
        mock_response = Mock()
        mock_response.json.return_value = {
            'id': 1,
            'name': '김철수',
            'age': 25
        }
        mock_get.return_value = mock_response
        
        # 테스트 실행
        service = ExternalService()
        result = service.get_user_data(1)
        
        # 검증
        self.assertEqual(result['name'], '김철수')
        mock_get.assert_called_once_with('https://api.example.com/users/1')

def main():
    unittest.main()

if __name__ == '__main__':
    main()
