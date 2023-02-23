using Server.Hubs;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddCors(options =>
{
    options.AddPolicy("CorsPolicy",
        policy =>
        {
            policy.AllowAnyHeader()
                  .AllowAnyMethod()
                  .SetIsOriginAllowed((host) => true)
                  .AllowCredentials();
        });
});

// Add services to the container.
builder.Services.AddRazorPages();
// TODO: https://learn.microsoft.com/en-us/aspnet/core/signalr/configuration?view=aspnetcore-7.0&tabs=dotnet
builder.Services.AddSignalR();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseCors("CorsPolicy");

// app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();
app.MapHub<ChatHub>("/chatHub");
app.MapHub<RoboticArmHub>("/robotic-arm-hub");

app.Run();
