const axios = require("axios");

// Kullanıcıdan URL'i isteme
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline.question("Lütfen test etmek istediğiniz URL'yi girin: ", async (url) => {
  // IP adreslerini içeren JSON verisi
  const data = {
    data: [
      { ipv4: "77.92.138.121" }, { ipv4: "212.102.38.46" }, { ipv4: "212.102.38.47" },
      { ipv4: "77.92.138.126" }, { ipv4: "77.92.138.120" }, { ipv4: "89.187.169.43" },
      { ipv4: "77.92.138.197" }, { ipv4: "185.107.83.119" }, { ipv4: "77.92.138.119" },
      { ipv4: "77.92.138.124" }, { ipv4: "109.236.91.24" }, { ipv4: "185.132.176.5" },
      { ipv4: "51.161.197.225" }, { ipv4: "51.79.231.108" }, { ipv4: "51.81.107.96" },
      { ipv4: "135.148.55.194" }, { ipv4: "185.73.200.202" }, { ipv4: "185.102.219.172" },
      { ipv4: "185.102.219.173" }, { ipv4: "195.181.165.181" }, { ipv4: "195.181.165.140" },
      { ipv4: "195.181.166.177" }, { ipv4: "185.76.9.154" }, { ipv4: "185.107.80.105" },
    ],
  };

  // Sonuçları depolamak için bir liste oluştur
  const results = [];

  for (const item of data.data) {
    const ip = item.ipv4;
    try {
      // Belirtilen URL'ye istek gönderme
      const response = await axios.get(url, { timeout: 5000 });
      // Yanıt kodunu kaydetme
      results.push({ ip, statusCode: response.status });
    } catch (error) {
      // Hata durumunda kaydetme
      results.push({ ip, statusCode: "Error", error: error.message });
    }
  }

  // Sonuçları yazdırma
  results.forEach((result) => {
    console.log(`IP: ${result.ip}, Status Code: ${result.statusCode}`);
  });

  readline.close();
});