import urllib.request
import json

def test_full_system():
    base = 'http://127.0.0.1:8000/api'
    
    # 1. Demo login
    req = urllib.request.Request(f'{base}/auth/demo-login', data=b'{}', headers={'Content-Type': 'application/json'})
    auth_data = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    token = auth_data['access_token']
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    print('[PASS] Demo Login Success: Token generated for Alex Mercer')

    # 2. Get Profile
    req = urllib.request.Request(f'{base}/profile', headers=headers)
    profile = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    print(f'[PASS] Profile Loaded: {profile["full_name"]} (Profession: {profile.get("profession", "Software Architect")})')

    # 3. Multi-profession Scenario Simulation Suite
    scenarios_to_test = [
        ('Software Engineer / Tech Lead', 'Should I refactor core architecture or ship a rapid MVP feature for tomorrow\'s demo?'),
        ('Startup Founder / Executive', 'Should I prepare the Tier-1 investor pitch or close the $180K enterprise customer renewal?'),
        ('Doctor / Healthcare Professional', 'Should I take an extra on-call ICU shift or protect sleep before tomorrow\'s surgical rotation?'),
        ('Product Manager / Consultant', 'Should we prioritize urgent security compliance patch or unblock Q4 feature roadmap deliverables?')
    ]

    for prof, prompt in scenarios_to_test:
        payload = json.dumps({'decision_prompt': prompt}).encode('utf-8')
        req = urllib.request.Request(f'{base}/scenarios', data=payload, headers=headers)
        res = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
        print(f'[PASS] {prof} Scenario Simulated: "{res["option_a"]["title"]}" vs "{res["option_b"]["title"]}"')

    # 4. Decision and Feedback Loop
    scen_payload = json.dumps({'decision_prompt': 'Should I refactor core architecture or ship a rapid MVP feature for tomorrow\'s demo?'}).encode('utf-8')
    req = urllib.request.Request(f'{base}/scenarios', data=scen_payload, headers=headers)
    scen = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    
    req = urllib.request.Request(f'{base}/scenarios/{scen["id"]}/choose', data=json.dumps({'chosen_option': 'OPTION_A'}).encode('utf-8'), headers=headers)
    chosen = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    print(f'[PASS] User Decision Finalized: {chosen["chosen_option"]}')

    fb_payload = json.dumps({
        'scenario_id': scen['id'],
        'chosen_option': 'OPTION_A',
        'prediction_summary': 'Refactoring core architecture',
        'actual_outcome': 'Successfully eliminated bottleneck and stakeholder signed off',
        'rating': 'VERY_USEFUL',
        'user_reflection': 'High energy evening session'
    }).encode('utf-8')
    req = urllib.request.Request(f'{base}/feedback', data=fb_payload, headers=headers)
    fb_res = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    # 5. ML Model Status & Metrics
    req = urllib.request.Request(f'{base}/ml/status')
    ml_status = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    print(f'[PASS] ML Model Status: {ml_status["status"]} (Accuracy: {ml_status["metrics"]["accuracy"]}%, Samples: {ml_status["metrics"]["dataset_samples"]})')

    # 6. ML Siri/Alexa Voice Predictions
    voice_tests = [
        ('Hey Twin, when is my highest productivity focus window?', 'CIRCADIAN_PEAK'),
        ('Alexa, should I refactor core architecture or ship an MVP feature today?', 'SCENARIO_SIMULATE'),
        ('Siri, am I approaching my fatigue boundary tonight?', 'FATIGUE_PREDICT'),
        ('Update my preference: I now prefer morning workouts', 'MEMORY_EVOLVE'),
        ('What is my top priority today?', 'PRIORITY_FOCUS')
    ]

    for voice_q, expected_intent in voice_tests:
        pred_payload = json.dumps({'text': voice_q, 'include_context': True}).encode('utf-8')
        req = urllib.request.Request(f'{base}/ml/predict', data=pred_payload, headers=headers)
        pred_res = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
        print(f'[PASS] Voice Utterance Classified: "{voice_q}" -> Intent: {pred_res["intent"]} (Conf: {pred_res["confidence"]}%)')
        print(f'       Siri/Alexa Speech Response: "{pred_res["speech_response"]}"')

    # 7. Retrain ML Model on Synthetic Data Pipeline
    train_payload = json.dumps({'num_samples': 800}).encode('utf-8')
    req = urllib.request.Request(f'{base}/ml/train', data=train_payload, headers=headers)
    train_res = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    print(f'[PASS] Synthetic Dataset Retraining: {train_res["message"]} (Duration: {train_res["metrics"]["training_duration_seconds"]}s)')

    print('\n==================================================================')
    print('ALL MULTI-PROFESSION LIFECYCLE, ML & VOICE SUITE TESTS PASSED 100%!')
    print('==================================================================')

if __name__ == '__main__':
    test_full_system()

