import logging
from django.http import JsonResponse
from django.views import View
from .data import QUESTION_DATA

logger = logging.getLogger(__name__)

VALID_GRADES = [9, 10, 11, 12]
VALID_COMPLEXITY = ['easy', 'medium', 'hard']


def health_check(request):
    # logger.debug("Health check requested")
    return JsonResponse({
        'service': 'english-service',
        'version': '1.0.0',
        'status': 'UP'
    })


class TopQuestionsByGradeView(View):
    def get(self, request, grade, n):
        logger.info("Fetching top %d English questions for grade %d", n, grade)

        if grade not in VALID_GRADES:
            # logger.warning("Invalid grade requested: %d", grade)
            return JsonResponse({'error': f'Invalid grade. Must be one of {VALID_GRADES}'}, status=400)
        if n <= 0 or n > 100:
            # logger.warning("Invalid n value requested: %d", n)
            return JsonResponse({'error': 'n must be between 1 and 100'}, status=400)

        questions = [q for q in QUESTION_DATA if q['grade'] == grade][:n]
        # logger.debug("Returning %d questions for grade %d", len(questions), grade)
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
            # logger.warning("Invalid n value requested: %d", n)
            return JsonResponse({'error': 'n must be between 1 and 100'}, status=400)

        questions = [q for q in QUESTION_DATA if q['topic'].lower() == topic.lower()][:n]
        # logger.debug("Returning %d questions for topic '%s'", len(questions), topic)
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
            # logger.warning("Invalid complexity requested: %s", complexity)
            return JsonResponse({'error': f'Invalid complexity. Must be one of {VALID_COMPLEXITY}'}, status=400)
        if n <= 0 or n > 100:
            # logger.warning("Invalid n value requested: %d", n)
            return JsonResponse({'error': 'n must be between 1 and 100'}, status=400)

        questions = [q for q in QUESTION_DATA if q['complexity'].lower() == complexity.lower()][:n]
        # logger.debug("Returning %d questions with complexity '%s'", len(questions), complexity)
        return JsonResponse({
            'subject': 'English',
            'complexity': complexity,
            'requested': n,
            'returned': len(questions),
            'questions': questions
        })


class QuestionsByGradeAndTopicView(View):
    def get(self, request, grade, topic, n):
        # logger.info("Fetching %d English questions for grade %d, topic: %s", n, grade, topic)

        if grade not in VALID_GRADES:
            # logger.warning("Invalid grade requested: %d", grade)
            return JsonResponse({'error': f'Invalid grade. Must be one of {VALID_GRADES}'}, status=400)

        questions = [q for q in QUESTION_DATA
                     if q['grade'] == grade and q['topic'].lower() == topic.lower()][:n]
        # logger.debug("Returning %d questions for grade %d, topic '%s'", len(questions), grade, topic)
        return JsonResponse({
            'subject': 'English',
            'grade': grade,
            'topic': topic,
            'returned': len(questions),
            'questions': questions
        })


class TopicsView(View):
    def get(self, request):
        # logger.info("Fetching all available English topics")
        topics = sorted(set(q['topic'] for q in QUESTION_DATA))
        # logger.debug("Returning %d topics", len(topics))
        return JsonResponse({'subject': 'English', 'topics': topics})


class StatsView(View):
    def get(self, request):
        # logger.info("Fetching question bank statistics")
        from collections import Counter
        grade_counts = Counter(q['grade'] for q in QUESTION_DATA)
        topic_counts = Counter(q['topic'] for q in QUESTION_DATA)
        complexity_counts = Counter(q['complexity'] for q in QUESTION_DATA)
        # logger.debug("Stats computed: total=%d, grades=%d, topics=%d, complexity_levels=%d",
        #              len(QUESTION_DATA), len(grade_counts), len(topic_counts), len(complexity_counts))
        return JsonResponse({
            'total_questions': len(QUESTION_DATA),
            'by_grade': dict(grade_counts),
            'by_topic': dict(topic_counts),
            'by_complexity': dict(complexity_counts),
        })
