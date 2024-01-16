from http import HTTPStatus

import pytest


@pytest.mark.asyncio
class TestDummy:
    async def test_inference(self, make_request):
        response = await make_request(method="POST", url=f"/")
        assert response.status == HTTPStatus.OK
