class ErrorsMessages:
    field_required = {'status': 'PS-0090', 'message': 'The field in blank is required'}
    register_failed = {'status': 'PS-0001', 'message': 'Error during user registration'}
    min_length = {'status': 'PS-0002','message': 'please your password must be min 8 characters'}
    registration_errors = {'min_length': min_length}
    max_length = {'status': 'PS-0003','message': 'please your password must be max 16 characters'}
    user_name_min = {'status': 'PS-0004', 'message': 'please your user name must be min 8 characters'}
    user_name_max = {'status': 'PS-0005', 'message': 'please your user name must be max 25 characters'}
