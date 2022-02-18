from my_app.data.repositories.portfolio_repository_impl import PortfolioRepositoryImpl


class TestPortfolioRepository:
    def test_get_portfolio(self):
        portfolio_repo = PortfolioRepositoryImpl()

        data = portfolio_repo.get_portfolio()

        assert data.personal_details is not None
        assert data.skills is not None

