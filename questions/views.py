import logging
from django.http import JsonResponse
from django.views import View
from .data import QUESTION_DATA

logger = logging.getLogger(__name__)

VALID_GRADES = [9, 10, 11, 12]
VALID_COMPLEXITY = ['easy', 'medium', 'hard']


def health_check(request):
    return JsonResponse({
        'service': 'english-service',
        'version': '1.0.0',
        'status': 'UP'
    })


class TopQuestionsByGradeView(View):
    def get(self, request, grade, n):
        logger.info("Fetching top %d English questions for grade %d", n, grade)

        if grade not in VALID_GRADES:
            return JsonResponse({'error': f'Invalid grade. Must be one of {VALID_GRADES}'}, status=400)
        if n <= 0 or n > 100:
            return JsonResponse({'error': 'n must be between 1 and 100'}, status=400)

        questions = [q for q in QUESTION_DATA if q['grade'] == grade][:n]
        return JsonResponse({
            'subject': 'English',
            'grade': grade,
            'requested': n,
            'returned': len(questions),
            'questions': questions
        })


class QuestionsByTopicView(View):
    def get(self, request, topic, n):
        logger.info("Fetching %d English questions for topic: %s", n, topic)

        if n <= 0 or n > 100:
            return JsonResponse({'error': 'n must be between 1 and 100'}, status=400)

        questions = [q for q in QUESTION_DATA if q['topic'].lower() == topic.lower()][:n]
        return JsonResponse({
            'subject': 'English',
            'topic': topic,
            'requested': n,
            'returned': len(questions),
            'questions': questions
        })


class QuestionsByComplexityView(View):
    def get(self, request, complexity, n):
        logger.info("Fetching %d English questions with complexity: %s", n, complexity)

        if complexity.lower() not in VALID_COMPLEXITY:
            return JsonResponse({'error': f'Invalid complexity. Must be one of {VALID_COMPLEXITY}'}, status=400)
        if n <= 0 or n > 100:
            return JsonResponse({'error': 'n must be between 1 and 100'}, status=400)

        questions = [q for q in QUESTION_DATA if q['complexity'].lower() == complexity.lower()][:n]
        return JsonResponse({
            'subject': 'English',
            'complexity': complexity,
            'requested': n,
            'returned': len(questions),
            'questions': questions
        })


class QuestionsByGradeAndTopicView(View):
    def get(self, request, grade, topic, n):
        if grade not in VALID_GRADES:
            return JsonResponse({'error': f'Invalid grade. Must be one of {VALID_GRADES}'}, status=400)

        questions = [q for q in QUESTION_DATA
                     if q['grade'] == grade and q['topic'].lower() == topic.lower()][:n]
        return JsonResponse({
            'subject': 'English',
            'grade': grade,
            'topic': topic,
            'returned': len(questions),
            'questions': questions
        })


class TopicsView(View):
    def get(self, request):
        topics = sorted(set(q['topic'] for q in QUESTION_DATA))
        return JsonResponse({'subject': 'English', 'topics': topics})


class StatsView(View):
    def get(self, request):
        from collections import Counter
        return JsonResponse({
            'total_questions': len(QUESTION_DATA),
            'by_grade': dict(Counter(q['grade'] for q in QUESTION_DATA)),
            'by_topic': dict(Counter(q['topic'] for q in QUESTION_DATA)),
            'by_complexity': dict(Counter(q['complexity'] for q in QUESTION_DATA)),
        })
