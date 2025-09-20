import datetime

def handler(request):
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Aviator Game - Bet7K</title>
  <link rel="icon" href="https://cdn-icons-png.flaticon.com/512/2965/2965339.png" type="image/png">
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Segoe UI', sans-serif;
    }

    body {
      background: linear-gradient(135deg, #1a1a2e, #0f3460);
      color: white;
      min-height: 100vh;
      padding: 20px;
      overflow-x: hidden;
    }

    .header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 15px 0;
      margin-bottom: 20px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }

    .logo {
      font-size: 1.8rem;
      background: linear-gradient(to right, #ff9a00, #ff5252);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      font-weight: 700;
    }

    .info {
      font-size: 0.9rem;
      opacity: 0.8;
    }

    .game-container {
      max-width: 400px;
      margin: 0 auto;
      border-radius: 15px;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
      background: rgba(0, 0, 0, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .iframe-wrapper {
      position: relative;
      padding-bottom: 56.25%; /* 16:9 */
      height: 0;
      overflow: hidden;
    }

    .iframe-wrapper iframe {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border: none;
      background: black;
    }

    .footer {
      margin-top: 20px;
      text-align: center;
      font-size: 0.8rem;
      opacity: 0.7;
      line-height: 1.5;
    }
  </style>
</head>
<body>
  <div class="header">
    <div class="logo">Aviator Bet7K</div>
    <div class="info">Atualizado em: {time}</div>
  </div>

  <div class="game-container">
    <div class="iframe-wrapper">
      <iframe src="https://m.888bets.co.mz" 
              frameborder="0"
              allowfullscreen
              style="border: none; background: black;">
        Seu navegador não suporta iframes.
      </iframe>
    </div>
  </div>

  <div class="footer">
    ⚠️ Jogue com responsabilidade.<br>
    Este site é apenas um portal de acesso ao jogo oficial.
  </div>
</body>
</html>
'''.replace('{time}', datetime.datetime.now().strftime('%H:%M:%S'))
    }
