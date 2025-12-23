using CLUniversity.Services;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();
builder.Services.AddServerSideBlazor();
builder.Services.AddSingleton<SchoolDataService>();
builder.Services.AddHttpClient<PaymentService>(client =>
{
    var backendUrl = Environment.GetEnvironmentVariable("BACKEND_URL") ?? "https://backend-dun-iota-65.vercel.app/";
    client.BaseAddress = new Uri(backendUrl);
    client.Timeout = TimeSpan.FromSeconds(30);
});

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseStaticFiles();
app.UseRouting();
app.MapBlazorHub();
app.MapFallbackToPage("/_Host");

app.Run();
