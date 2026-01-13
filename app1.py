<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório CESUPE</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .header {
            background: linear-gradient(135deg, #1f4788 0%, #2c5aa0 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .header h1 {
            margin: 0 0 10px 0;
            font-size: 28px;
        }
        .header p {
            margin: 5px 0;
            opacity: 0.9;
        }
        .registro {
            background: white;
            padding: 25px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            border-left: 5px solid #2c5aa0;
        }
        .registro-header {
            background-color: #e8f4f8;
            padding: 15px;
            margin: -25px -25px 20px -25px;
            border-radius: 8px 8px 0 0;
            border-bottom: 2px solid #2c5aa0;
        }
        .registro-header h2 {
            margin: 0;
            color: #1f4788;
            font-size: 20px;
        }
        .registro-tipo {
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: bold;
            margin-left: 10px;
        }
        .tipo-atendimento {
            background-color: #4CAF50;
            color: white;
        }
        .tipo-horas {
            background-color: #FF9800;
            color: white;
        }
        .tipo-erro {
            background-color: #f44336;
            color: white;
        }
        .campo {
            margin: 12px 0;
            display: flex;
            border-bottom: 1px solid #eee;
            padding-bottom: 8px;
        }
        .campo-label {
            font-weight: bold;
            color: #1f4788;
            min-width: 150px;
            margin-right: 15px;
        }
        .campo-valor {
            color: #333;
            flex: 1;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            color: #666;
            border-top: 2px solid #ddd;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>📊 RELATÓRIO DE REGISTROS - CESUPE</h1>
        <p>Sistema de Controle de Bastão</p>
        <p><strong>Gerado em:</strong> 13/01/2026 às 16:30:45</p>
        <p><strong>Total de registros:</strong> 3</p>
    </div>

    <div class="registro">
        <div class="registro-header">
            <h2>📝 REGISTRO #1 <span class="registro-tipo tipo-atendimento">ATENDIMENTO</span></h2>
        </div>
        
        <div class="campo">
            <div class="campo-label">📅 Data/Hora:</div>
            <div class="campo-valor">13/01/2026 09:15:30</div>
        </div>
        <div class="campo">
            <div class="campo-label">👤 Consultor:</div>
            <div class="campo-valor">Alex Paulo da Silva</div>
        </div>
        <div class="campo">
            <div class="campo-label">👥 Usuário:</div>
            <div class="campo-valor">Cartório</div>
        </div>
        <div class="campo">
            <div class="campo-label">🏢 Setor:</div>
            <div class="campo-valor">1ª Vara Cível</div>
        </div>
        <div class="campo">
            <div class="campo-label">💻 Sistema:</div>
            <div class="campo-valor">Eproc</div>
        </div>
        <div class="campo">
            <div class="campo-label">📝 Descrição:</div>
            <div class="campo-valor">Dúvida sobre petição inicial</div>
        </div>
        <div class="campo">
            <div class="campo-label">📞 Canal:</div>
            <div class="campo-valor">Telefone</div>
        </div>
        <div class="campo">
            <div class="campo-label">✅ Desfecho:</div>
            <div class="campo-valor">Resolvido - Cesupe</div>
        </div>
    </div>

    <div class="registro">
        <div class="registro-header">
            <h2>⏰ REGISTRO #2 <span class="registro-tipo tipo-horas">HORAS EXTRAS</span></h2>
        </div>
        
        <div class="campo">
            <div class="campo-label">📅 Data/Hora:</div>
            <div class="campo-valor">13/01/2026 18:30:00</div>
        </div>
        <div class="campo">
            <div class="campo-label">👤 Consultor:</div>
            <div class="campo-valor">Marina Silva Marques</div>
        </div>
        <div class="campo">
            <div class="campo-label">📅 Data:</div>
            <div class="campo-valor">13/01/2026</div>
        </div>
        <div class="campo">
            <div class="campo-label">🕐 Início:</div>
            <div class="campo-valor">18:00</div>
        </div>
        <div class="campo">
            <div class="campo-label">⏱️ Tempo Total:</div>
            <div class="campo-valor">2h30</div>
        </div>
        <div class="campo">
            <div class="campo-label">📝 Motivo:</div>
            <div class="campo-valor">Finalização de relatório mensal</div>
        </div>
    </div>

    <div class="registro">
        <div class="registro-header">
            <h2>🐛 REGISTRO #3 <span class="registro-tipo tipo-erro">ERRO/NOVIDADE</span></h2>
        </div>
        
        <div class="campo">
            <div class="campo-label">📅 Data/Hora:</div>
            <div class="campo-valor">13/01/2026 14:20:15</div>
        </div>
        <div class="campo">
            <div class="campo-label">👤 Consultor:</div>
            <div class="campo-valor">Hugo Oliveira Santos</div>
        </div>
        <div class="campo">
            <div class="campo-label">📌 Título:</div>
            <div class="campo-valor">Erro ao gerar relatório no sistema</div>
        </div>
        <div class="campo">
            <div class="campo-label">🎯 Objetivo:</div>
            <div class="campo-valor">Gerar relatório mensal de atendimentos</div>
        </div>
        <div class="campo">
            <div class="campo-label">🧪 Relato:</div>
            <div class="campo-valor">Sistema apresenta erro 500 ao tentar gerar relatório</div>
        </div>
        <div class="campo">
            <div class="campo-label">🏁 Resultado:</div>
            <div class="campo-valor">Chamado aberto, aguardando correção</div>
        </div>
    </div>

    <div class="footer">
        <p>Sistema de Controle de Bastão - CESUPE/TJMG</p>
        <p>Relatório gerado automaticamente</p>
    </div>
</body>
</html>
