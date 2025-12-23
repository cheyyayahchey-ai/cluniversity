using System.Net.Http.Json;
using System.Text.Json.Serialization;
using CLUniversity.Models;

namespace CLUniversity.Services;

public class PaymentService
{
    private readonly HttpClient _httpClient;

    public PaymentService(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    public async Task<QRCodeResult> GenerateQRCode(decimal amount, string currency, string paymentType, string studentId)
    {
        try
        {
            var response = await _httpClient.PostAsJsonAsync("api/payments/generate-qr", new
            {
                amount = amount,
                currency = currency,
                payment_type = paymentType,
                student_id = studentId
            });

            if (response.IsSuccessStatusCode)
            {
                var result = await response.Content.ReadFromJsonAsync<PythonQRResponse>();
                if (result?.Success == true)
                {
                    return new QRCodeResult
                    {
                        Success = true,
                        QrImage = result.QrImage ?? "",
                        Md5 = result.Md5 ?? "",
                        BillNumber = result.BillNumber ?? ""
                    };
                }
            }
            var error = await response.Content.ReadAsStringAsync();
            return new QRCodeResult { Success = false, Error = error };
        }
        catch (Exception ex)
        {
            return new QRCodeResult { Success = false, Error = ex.Message };
        }
    }

    public async Task<bool> CheckPaymentStatus(string md5)
    {
        try
        {
            var response = await _httpClient.PostAsJsonAsync("api/payments/check", new { md5 });
            if (response.IsSuccessStatusCode)
            {
                var result = await response.Content.ReadFromJsonAsync<PaymentCheckResponse>();
                return result?.Paid == true;
            }
            return false;
        }
        catch
        {
            return false;
        }
    }

    public static decimal ConvertToKHR(decimal usd) => Math.Round(usd * 4100);
    public static string FormatUSD(decimal amount) => $"${amount:N2}";
    public static string FormatKHR(decimal amount) => $"៛{amount:N0}";
}

public class PythonQRResponse
{
    [JsonPropertyName("success")]
    public bool Success { get; set; }
    
    [JsonPropertyName("qr_image")]
    public string? QrImage { get; set; }
    
    [JsonPropertyName("qr_data")]
    public string? QrData { get; set; }
    
    [JsonPropertyName("md5")]
    public string? Md5 { get; set; }
    
    [JsonPropertyName("bill_number")]
    public string? BillNumber { get; set; }
}

public class PaymentCheckResponse
{
    [JsonPropertyName("success")]
    public bool Success { get; set; }
    
    [JsonPropertyName("status")]
    public string? Status { get; set; }
    
    [JsonPropertyName("paid")]
    public bool Paid { get; set; }
}
