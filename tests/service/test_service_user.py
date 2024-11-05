from src.service.service_user import ServiceUser

class TestServiceUser:

    def test_add_user_success(self):
        name_add = 'Leonardo'
        job_add = 'TechLead'
        result_expect = 'Usuario adicionado com sucesso'
        service = ServiceUser()

        result = service.add_user(name=name_add, job=job_add)

        assert result_expect == result

    def test_validate_null_job(self):
        name_null = 'Matheus'
        job_null = None
        result_expect = 'Usuario nao adicionado'
        service = ServiceUser()

        result = service.add_user(name=name_null, job=job_null)

        assert result_expect == result

    def test_add_user_name_invalid(self):
        name_invalid = 123
        job_add = 'TechLead'
        result_expect = 'Nome ou Profissão precisa ser um texto'
        service = ServiceUser()

        result = service.add_user(name=name_invalid, job=job_add)

        assert result_expect == result

    def test_add_user_job_invalid(self):
        name_add = 'Lavinia'
        job_invalid = 1234
        result_expect = 'Nome ou Profissão precisa ser um texto'
        service = ServiceUser()

        result = service.add_user(name=name_add, job=job_invalid)

        assert result_expect == result

    def test_no_add_user(self):
        name_add = 'Lavinia'
        job_add = None
        result_expect = 'Usuario nao adicionado'
        service = ServiceUser()

        result = service.add_user(name=name_add, job=job_add)

        assert result_expect == result

    def test_dell_user(self):
        user_bd = 'Lavinia'
        result_expect = 'Usuario removido'
        service = ServiceUser()

        result = service.del_user(name=user_bd)

        assert result_expect == result 

    def test_no_dell_user(self):
        user_bd_invalid = None
        result_expect = 'Usuario não encontrado'
        service = ServiceUser()

        result = service.del_user(name=user_bd_invalid)

        assert result_expect == result   

    def test_update_user(self):
        user_bd = 'Lavinia'
        job_update = 'Estudante'
        result_expect = 'Profissão atualizada com sucesso'
        service = ServiceUser()

        result = service.update_user(name=user_bd,new_job=job_update)

        assert result_expect == result

    def test_no_update_user(self):
        user_bd = 'Michele'
        job_update = 'Estudante'
        result_expect = 'Usuario não encontrado'
        service = ServiceUser()

        result = service.update_user(name=user_bd,new_job=job_update)

        assert result_expect == result

    def test_select_user(self):
        user_bd = 'Lavinia'
        job = 'Tester'
        result_expect = 'Profissão: ' + job
        service = ServiceUser()

        result = service.select_user(name=user_bd)

        assert result_expect == result

    def test_no_select_user(self):
        user_bd = 'Lucas'
        job = 'Tester'
        result_expect = 'Usuario não encontrado'
        service = ServiceUser()

        result = service.select_user(name=user_bd)

        assert result_expect == result