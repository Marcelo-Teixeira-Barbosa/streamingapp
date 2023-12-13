from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    urls_to_extract = [
        'http://127.0.0.1:8003/graphql',
        'http://127.0.0.1:8001',
        'http://localhost:8000/?wsdl',
    ]

    @task
    def extract_links(self):
        for url in self.urls_to_extract:
            self.client.get(url)

    def on_stop(self):
        import os

        if os.path.exists("results_stats.csv"):
            num_users = str(self.environment.parsed_options.num_users)
            spawn_rate = str(self.environment.parsed_options.spawn_rate)
            run_time = str(self.environment.parsed_options.run_time)
            csv_name = num_users + "_users_for_spawn_rate_" + spawn_rate + "_run_time_" + run_time + "_results_stats.csv"
            os.rename("results_stats.csv", csv_name)
