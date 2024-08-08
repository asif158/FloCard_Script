import requests
import time
import plotly.express as px
import pandas as pd

def check_load_time(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        response.raise_for_status()
        end_time = time.time()
        load_time = end_time - start_time
        return load_time, True
    except requests.exceptions.RequestException as e:
        print(f"Error for URL {url}: {e}")
        return None, False

def update_dashboard(data):
    df = pd.DataFrame(data, columns=['URL', 'Load Time (s)', 'Status'])
    df_success = df[df['Status'] == 'Success']
    df_failure = df[df['Status'] == 'Failed']
    
    fig = px.bar(df_success, x='URL', y='Load Time (s)', title='Website Load Times', color='Status', color_discrete_map={'Success': 'green'})
    fig.add_bar(x=df_failure['URL'], y=[0]*len(df_failure), name='Failed: ' + str(len(df_failure)), marker=dict(color='red'))
    fig.add_bar(x=df['URL'], y=[0]*len(df), name='Total URLs: ' + str(len(df)), marker=dict(color='blue'))

    for idx, row in df_failure.iterrows():
        fig.add_annotation(
            x=row['URL'], y=0, text='Failed', showarrow=False, yshift=10, font=dict(color='red')
        )
    
    fig.show()

def main(urls):
    results = []
    best_load_time = float('inf')
    worst_load_time = 0
    best_urls = []
    worst_urls = []

    for url in urls:
        load_time, success = check_load_time(url)
        status = 'Success' if success else 'Failed'
        if load_time is not None:
            results.append((url, load_time, status))
            if load_time < best_load_time:
                best_load_time = load_time
                best_urls = [url]
            elif load_time == best_load_time:
                best_urls.append(url)
                
            if load_time > worst_load_time:
                worst_load_time = load_time
                worst_urls = [url]
            elif load_time == worst_load_time:
                worst_urls.append(url)
        else:
            results.append((url, 0, status))
        
        print(f"URL: {url}, Load Time: {load_time:.2f} seconds" if success else f"URL: {url}, Load Time: Failed to load")

    print("\nWorst Load Time:")
    for url in worst_urls:
        print(f"URL: {url}, Load Time: {worst_load_time:.2f} seconds")

    print("\nBest Load Time:")
    for url in best_urls:
        print(f"URL: {url}, Load Time: {best_load_time:.2f} seconds")
    
    update_dashboard(results)

if __name__ == "__main__":
    base_url = 'https://flocard.app'
    endpoints = [
        "/",
        "/AboutUs",
        "/Projects",
        "/PlantersApp",
        "/PlantersApp#PlantersAppForBusiness",
        "/PlantersApp#PlantersAppForPlanters",
        "/Flocardforcommunity",
        "/FlocardForCommunity#ClimateFinance",
        "/FlocardForCommunity#ProjectFeasibility",
        "/FlocardForCommunity#ProjectDesign",
        "/FlocardForCommunity#VoluntaryCarbonMarket",
        "/FlocardForBusiness",
        "/FlocardForBusiness#CarbonOffsetting",
        "/FlocardForBusiness#BusinessDashboard",
        "/FlocardForBusiness#NetZero",
        "/FlocardForBusiness#GHGCalculator",
        "/FlocardForBusiness#SDGAlignment",
        "/FlocardForBusiness#AvoidanceProjectDevelopment",
        "/ContactUs",
        "/SupportHome",
        "/Blogs",
        "/knowledgebank",
        "/IntegratedSolutions",
        "/ImpactingSDGs",
        "/FAQ",
        "/Newsletters",
        "/PrivacyPolicy",
        "/Disclaimer",
        "/ReleaseNotes",
    ]

    urls = [base_url + endpoint for endpoint in endpoints]
    main(urls)
