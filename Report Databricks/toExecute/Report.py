# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC ![Unive logo](assets/logo_caFoscari.png "Università Ca'Foscari di Venezia")
# MAGIC 
# MAGIC # Analisi della sicurezza attraverso lo studio di indici
# MAGIC 
# MAGIC L’attività presentata consiste nell’analizzare il livello di sicurezza informatica di un ecosistema attraverso il calcolo e l’interpretazione di indici. Questi verranno suddivisi in tre categorie principali: di **Conformità**, di **Andamento** e di **Anomalia**.
# MAGIC 
# MAGIC  > ##### Conformità
# MAGIC  >
# MAGIC  >  Un indice di conformità rappresenta una **valutazione della conformità** dell’ambiente di studio rispetto ad un determinato target. 
# MAGIC 
# MAGIC  > ##### Andamento
# MAGIC  >
# MAGIC  >  Gli indici di andamento possono essere considerati come i parametri più significativi essendo di immediata comprensione. Rappresentano **l’andamento** di una particolare **attività** in un determinato periodo.
# MAGIC 
# MAGIC  > ##### Anomalia
# MAGIC  >
# MAGIC  >  Un indice di anomalia invece consiste in una valutazione appositamente creata per identificare anomalie. Si analizzano i **comportamenti** dei soggetti all’interno dell’ambiente di studio e si individuano potenziali **anomalie** rispetto ad un valore atteso. 
# MAGIC 
# MAGIC ***
# MAGIC 
# MAGIC ## Metodologia e approccio
# MAGIC 
# MAGIC In questa sezione verrà descritta la metodologia utilizzata per portare a termine l'attività. Questa può essere riassunta in tre fasi, qui di seguito è presente una descrizione dettagliata per ognuna di queste. 
# MAGIC 
# MAGIC 
# MAGIC ##### 1.  Prima fase -  Tecnologie
# MAGIC     L’attività principale della prima fase è stata di studio delle tecnologie utilizzate. 
# MAGIC         - Microsoft Azure e Azure Portal
# MAGIC         - Log Analytics e Azure Monitor
# MAGIC         - Microsoft Sentinel
# MAGIC         
# MAGIC     Altre tecnologie sono state utilizzate indirettamente tra cui MITRE ATT&K framework e Jupyter/Databricks notebook.
# MAGIC 
# MAGIC ##### 2.  Seconda fase - Analisi
# MAGIC     La seconda fase comprende uno studio preliminare alla teoria degli indici e sulla distinzione tra KPI e KRI.
# MAGIC     
# MAGIC     Successivamente è stata fatta un analisi dei dati per la selezione di quali indici generare.
# MAGIC     
# MAGIC     I dati analizzati provengono da ambienti Sentinel di dimostrazione (Demo) e da ambienti Sentinel gestiti da Horizon Security s.r.l.
# MAGIC 
# MAGIC ##### 3.  Terza fase - Calcolo
# MAGIC     La terza ed ultima fase consiste nel calcolo degli indici precedentemente scelti e nella produzione di un grafico che permette una rappresentazione grafica dell’indice stesso.
# MAGIC     
# MAGIC     Ogni grafico è corredato da una serie di considerazioni sui risultati e da una serie di proposte per la correzione di eventuali problematiche.
# MAGIC 
# MAGIC ***
# MAGIC 
# MAGIC ## Tecnologie utilizzate
# MAGIC 
# MAGIC ##### - Microsoft Azure
# MAGIC     Microsoft Azure è la piattaforma cloud pubblica di Microsoft, che offre servizi di cloud computing.
# MAGIC     
# MAGIC     Tramite Azure vengono erogati servizi appartenenti a diverse categorie quali:
# MAGIC         - risorse di elaborazione
# MAGIC         - archiviazione e memorizzazione dati
# MAGIC         - trasmissione dati e interconnessione di reti
# MAGIC         - analisi e apprendimento automatico
# MAGIC         - sicurezza e gestione delle identità
# MAGIC         
# MAGIC     I servizi messi a disposizione da Microsoft Azure possono essere classificati in tre aree, a seconda della modalità di erogazione adottata: Infrastructure as a Service (IaaS), Platform as a Service (PaaS) e infine Software as a Service (SaaS). 
# MAGIC    ![Matrice di responsabilità](/assets/mat_resp.png "Distribuzione delle responsabilità")
# MAGIC    
# MAGIC    
# MAGIC ##### - Microsoft Sentinel
# MAGIC     I dati con i quali sono stati sviluppati gli indici provengono da Microsoft Sentinel.
# MAGIC     
# MAGIC     Microsoft Sentinel è una soluzione di orchestrazione, automazione e risposta ( SOAR) scalabile, nativa del cloud, per la gestione delle informazioni e degli eventi di sicurezza (SIEM, Security Orchestration, Automation, and Response).
# MAGIC     
# MAGIC     Offre analisi della sicurezza intelligente e intelligence per le minacce in tutta l'azienda, offrendo un'unica soluzione per il rilevamento degli attacchi, la visibilità delle minacce, la ricerca proattiva e la risposta alle minacce.
# MAGIC 
# MAGIC ***
# MAGIC 
# MAGIC ## Analisi dei dati
# MAGIC 
# MAGIC > ‹‹ Microsoft Sentinel è la visione d'occhio dell'azienda che attenua lo stress degli attacchi sempre più sofisticati ››
# MAGIC 
# MAGIC ##### - Provenienza
# MAGIC     Sentinel raccoglie i dati su scala cloud per tutti gli utenti, i dispositivi, le applicazioni e l'infrastruttura, in locale e in più cloud.
# MAGIC     Microsoft Sentinel include una serie di connettori per le principali soluzioni Microsoft:
# MAGIC         - Office 365
# MAGIC         - Azure AD 
# MAGIC         - Microsoft Defender for Identity 
# MAGIC         - Microsoft Defender for Cloud Apps
# MAGIC         - Microsoft Defender for Endpoint 
# MAGIC         
# MAGIC     Inoltre, sono presenti connettori predefiniti a soluzioni non Microsoft, per l'ecosistema di sicurezza allargato. 
# MAGIC     È anche possibile usare il formato di evento comune, Syslog o REST-API per connettere le origini dati anche a Microsoft Sentinel.
# MAGIC 
# MAGIC    
# MAGIC    
# MAGIC ##### - Struttura dei dati
# MAGIC     Microsoft Sentinel incorpora in modo nativo il servizio Log Analytics. Log Analytics è uno strumento che consente di eseguire query sui dati raccolti dai log di Monitoraggio di Azure e analizzarne i risultati in modo interattivo.
# MAGIC     
# MAGIC     Microsoft Sentinel arricchisce l'analisi e il rilevamento con l'intelligenza artificiale e fornisce il flusso di intelligence sulle minacce di Microsoft e consente di ottenere informazioni sulle minacce.
# MAGIC     
# MAGIC     I dati provenienti dall’analisi dei file di Log vengono memorizzati all’interno dell’ambiente Microsoft Sentinel sotto forma di tabelle.
# MAGIC     Questa base di dati è interrogabile attraverso un linguaggio di interrogazione chiamato Kusto (KQL).
# MAGIC 
# MAGIC     KQL funziona con uno schema organizzato tramite una gerarchia simile a quella di SQL: database, tabelle e colonne.
# MAGIC     Infatti KQL non è altro che un dialetto di SQL.
# MAGIC 
# MAGIC ***
# MAGIC 
# MAGIC ## Calcolo dei dati
# MAGIC 
# MAGIC In questa sezione vedremo quali sono gli indici scelti e ne vedremo il loro calcolo e una loro rappresentazione grafica.

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### 1. Monitor sui tentativi di MFA falliti
# MAGIC 
# MAGIC Questo è un **indice di anomalia** e successivamente verrà mostrato un grafico contenente i tentativi di login falliti a causa della fallita autenticazione a due fattori (MFA) degli ultimi 5 giorni, raggruppati in base all’ora.
# MAGIC 
# MAGIC Si riesce a notare che il girono 5/03/2022 alle 00:00:00 c’è stato un insolito picco di tentativi che si sono conclusi con un fallimento dell’autenticazione a due fattori.
# MAGIC 
# MAGIC La query KQL relativa a questi dati è: 
# MAGIC 
# MAGIC ```
# MAGIC SignInLogs
# MAGIC | where TimeGenerated > ago(5d)
# MAGIC | where ResultDescription has "not pass the MFA"
# MAGIC | summarize Count=count() by bin(TimeGenerated, 1h)
# MAGIC ```

# COMMAND ----------

# MAGIC %sql
# MAGIC select Time, count(*) as Count 
# MAGIC from default.mfafailedaccess
# MAGIC where ResultDescription like "%not pass the MFA%"
# MAGIC group by Time
# MAGIC order by Time

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ##### Considerazioni
# MAGIC     Questo picco potrebbe essere causato da un tentativo di brute force del secondo fattore a seguito di un furto di credenziali da parte di un attaccante.
# MAGIC     
# MAGIC     Le possibili azioni correttive a valle di un indagine sono:
# MAGIC         - Blocco dell’account compromesso
# MAGIC         - Rifiuto di ulteriori tentativi di connessione da quell’indirizzo IP
# MAGIC 
# MAGIC ***

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### 2. Monitor sui tentativi di login
# MAGIC 
# MAGIC Anche questo è un **indice di anomalia** e verrà mostrato un grafico contenente il conteggio dei tentativi di login degli ultimi 3 giorni. Vengono poi raggruppati in base all’ora.
# MAGIC 
# MAGIC Questo grafico sarebbe del tutto in linea con un contesto lavorativo ma presenta un anomalia, c’è stato un insolito tentativo di accessi in un orario notturno (14/03/2022, 23:00:00).
# MAGIC 
# MAGIC La query KQL relativa a questi dati è:
# MAGIC    ```
# MAGIC    SignInLogs
# MAGIC    | where TimeGenerated > ago(3d)
# MAGIC    | summarize LoginCount=count() by bin(TimeGenerated, 1h)
# MAGIC    ```

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC CREATE VIEW count_login
# MAGIC AS( select TimeGenerated, count(TimeGenerated) as LoginCount
# MAGIC     from loginattempts
# MAGIC     group by TimeGenerated )

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select Date, LoginCount
# MAGIC from plaindate left join count_login on plaindate.Date = count_login.TimeGenerated
# MAGIC where Date between DATE'2022-03-14' and DATE'2022-03-17'
# MAGIC order by Date

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ##### Considerazioni
# MAGIC     Questo potrebbe rappresentare un tentativo da parte di un attaccante di avere accesso ad un sistema tramite un attacco di brute force delle credenziali di accesso.
# MAGIC 
# MAGIC     Le possibili azioni correttive a valle di un indagine sono:
# MAGIC         - Aggiungere più fattori di autenticazione nelle ore notturne.
# MAGIC         - Aggiungere un limite massimo ai tentativi di login.
# MAGIC 
# MAGIC 
# MAGIC ***

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### 3. Monitor sulle attività di rete
# MAGIC 
# MAGIC Un ultimo **indice di anomalia** dove il seguente grafico analizza l’attività di rete effettiva (blu) e le paragona ad un’attività di rete standard (rosso). 
# MAGIC 
# MAGIC 
# MAGIC Si nota che il traffico di rete è elevato anche nelle ore notturne tra il 12 e il 13 e tra il 13 e il 14 marzo 2022. 
# MAGIC 
# MAGIC Le attività di rete rimangono sotto la soglia di detection (nessun picco troppo elevato) ma costanti anche durante la notte.

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select act.TimeGenerated, act.Actual_Count, exp.Expected_Count 
# MAGIC from processes_actual_trend as act 
# MAGIC   inner join processes_expected_trend as exp on act.TimeGenerated = exp.TimeGenerated
# MAGIC order by act.TimeGenerated

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ##### Considerazioni
# MAGIC     In questo caso potrebbe esserci il rischio di esfiltrazione di informazioni sensibili. Un attaccante mantiene delle comunicazioni attive per esportare dati.
# MAGIC 
# MAGIC     Le possibili azioni correttive a valle di un indagine sono:
# MAGIC         - Bloccare le comunicazioni verso l’indirizzo/gli indirizzi IP
# MAGIC         - Implementare sistemi di encryption dei dati
# MAGIC 
# MAGIC 
# MAGIC ***

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### 4. Trend dei processi eseguiti
# MAGIC 
# MAGIC Questo primo **indice di andamento** studia e analizza il conteggio delle esecuzioni dei processi nell’arco di un mese.
# MAGIC 
# MAGIC Nella tabella SecurityEvent, presente in Microsoft Sentinel, l’identificatore dell’evento riguardante l’esecuzione di un processo è 4688.
# MAGIC 
# MAGIC La query KQL relativa a questi dati è:
# MAGIC    ```
# MAGIC    SecurityEvent
# MAGIC    | where TimeGenerated > ago(30d)
# MAGIC    | where EventID == 4688
# MAGIC    | summarize Process_Count=count() by bin(TimeGenerated, 1h)
# MAGIC    ```

# COMMAND ----------

# MAGIC %sql 
# MAGIC 
# MAGIC select Time as Date, Process_Count 
# MAGIC from processexecution
# MAGIC order by Time

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ##### Considerazioni
# MAGIC     Possiamo notare che il trend dei processi eseguiti è costante, non si presuppone l’esistenza di un attività sospetta. Non c’è necessità di ulteriori indagini.
# MAGIC 
# MAGIC     Nessuna azione correttiva è necessaria.
# MAGIC 
# MAGIC 
# MAGIC ***

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### 5. Trend dei password / name reset
# MAGIC 
# MAGIC Un ulteriore **indice di andamento** ci mostra il trend relativo ai reset della password e del nome dei profili monitorati da Sentinel.
# MAGIC 
# MAGIC Si nota che il numero di reset è costante a fine mese, plausibile considerando alcune policy di sicurezza aziendale. Nei giorni compresi tra il 14 e il 17 marzo invece c’è un attività sospetta. 
# MAGIC 
# MAGIC La query KQL relativa a questi dati è:
# MAGIC    ```
# MAGIC    SecurityEvent
# MAGIC    | where TimeGenerated > ago(100d)
# MAGIC    | where EventID in (4723, 4724, 4781)
# MAGIC    | summarize Count=count() by bin(TimeGenerated, 1h)
# MAGIC    ```

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC CREATE VIEW count_password_reset
# MAGIC AS( select DateTime, count(DateTime) as ResetCount
# MAGIC     from resetpassword
# MAGIC     where EventID in (4723, 4724, 4781)
# MAGIC     group by DateTime )

# COMMAND ----------

# MAGIC %sql
# MAGIC select Date, ResetCount
# MAGIC from plaindate left join count_password_reset on plaindate.Date = count_password_reset.DateTime
# MAGIC where Date > DATE'2021-12-28'

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ##### Considerazioni
# MAGIC     Questa attività potrebbe essere sintomo di tentativo di movimento laterale da parte di un attaccante.
# MAGIC     Quest’ultimo infatti cercherà di rendere inaccessibili i profili utente di cui ha appena ottenuto le credenziali di accesso.
# MAGIC 
# MAGIC     Le possibili azioni sono:
# MAGIC         - Stabilire regole più rigorose sulla generazione delle credenziali.
# MAGIC         - Sensibilizzare i dipendenti su tematiche phishing ed esposizione delle credenziali.
# MAGIC 
# MAGIC ***

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### 6. Rapporto tra tentativi di login totali e falliti
# MAGIC 
# MAGIC Nel nostro primo **indice di conformità** viene rappresentato un **grafico a dispersione** che mostra una relazione lineare tra il numero tentativi di login totali e i tentativi di login falliti. 
# MAGIC 
# MAGIC All’aumentare dell’uno è visibile un aumento dell’altro.
# MAGIC 
# MAGIC Sono presenti alcuni punti nel grafico in cui è presente un numero di login falliti sospetto. 
# MAGIC 
# MAGIC La query KQL relativa a quest grafico è:
# MAGIC    ```
# MAGIC SigninLogs
# MAGIC | where TimeGenerated > ago(100d)
# MAGIC | summarize Count_Tot=count() by Tot=bin(TimeGenerated, 1d)
# MAGIC | join kind=inner(
# MAGIC SigninLogs
# MAGIC | where TimeGenerated > ago(100d)
# MAGIC | where ResultType != 0
# MAGIC | summarize Count_Fail=count() by bin(TimeGenerated, 1d)) on $left.Tot==$right.TimeGenerated
# MAGIC | project-away Tot, TimeGenerated
# MAGIC | order by Count_Tot asc
# MAGIC    ```

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC CREATE OR REPLACE VIEW count_failed_login
# MAGIC AS( select Date, count(Date) as CountFailed
# MAGIC     from linearregression
# MAGIC     where ResultType != 0
# MAGIC     group by Date )

# COMMAND ----------

# MAGIC %sql
# MAGIC select *
# MAGIC from linearregression
# MAGIC order by Count_Tot

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ##### Considerazioni
# MAGIC 
# MAGIC     Queste anomalie potrebbero essere causate da un dictionary attack dove si cerca di avere accesso al sistema tramite brute force.
# MAGIC 
# MAGIC     Le possibili azioni sono:
# MAGIC         - Indagare sulla causa del picco di tentativi falliti.
# MAGIC         - Assicurarsi che l’attacco non abbia avuto esito positivo.
# MAGIC 
# MAGIC 
# MAGIC ***

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### 7. Controllo sull'integrità delle e-mail
# MAGIC 
# MAGIC Un ulteriore **indice di conformità** viene rappresentato tramite un grafico ad anello che mostra qual è la destinazione delle e-mail in arrivo sulle caselle postali istituzionali.
# MAGIC  
# MAGIC 
# MAGIC I risultati sono calcolati sulla base dell’azione finale intrapresa su un e-mail. Può derivare dal verdetto del filtro, dalle policies in vigore o dall’azione dell’utente.
# MAGIC  
# MAGIC 
# MAGIC La query KQL relativa a quest grafico è:
# MAGIC    ```
# MAGIC EmailEvents
# MAGIC | where TimeGenerated > ago(100d)
# MAGIC | where isnotempty(EmailAction)
# MAGIC | summarize Count=count() by EmailAction
# MAGIC    ```

# COMMAND ----------

# MAGIC %sql 
# MAGIC select EmailAction, count(*) as Count
# MAGIC from emailevents
# MAGIC group by EmailAction

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ##### Considerazioni
# MAGIC 
# MAGIC     Si può notare che circa il 22% viene mandato tra le junk mail mentre solo il 10% viene effettivamente riconosciuto come pericoloso e mandato in quarantena.
# MAGIC     
# MAGIC     Potrebbero essere presenti delle e-mail pericolose non trattate come tali.
# MAGIC 
# MAGIC 
# MAGIC     Le azioni a riguardo possono essere:
# MAGIC         - Rivisitazione dei criteri del filtro per e-mail
# MAGIC         - Sensibilizzazione dei dipendenti sul phishing.
# MAGIC 
# MAGIC 
# MAGIC ***

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### 8. Stato di protezione dei dispositivi
# MAGIC 
# MAGIC Questo ultimo indice è un **indice di conformità** e mostra il totale dei dispositivi monitorati dall’ambiente Sentinel, li suddivide in base al sistema operativo e ne mostra lo stato di protezione. 
# MAGIC 
# MAGIC Questo stato di protezione è dato dal livello di aggiornamento del dispositivo. Si può considerare un dispositivo protetto come un dispositivo correttamente configurato e aggiornato.
# MAGIC 
# MAGIC La query KQL relativa a quest grafico è:
# MAGIC ```
# MAGIC ProtectionStatus
# MAGIC | where TimeGenerated > ago(100d)
# MAGIC | summarize Out_of_date=dcount(SourceComputerId) by ProtectionStatus, OSName, TypeofProtection
# MAGIC | where ProtectionStatus has "out of date"
# MAGIC | project OSName, Out_of_date
# MAGIC | union (
# MAGIC   ProtectionStatus
# MAGIC   | where TimeGenerated > ago(100d)
# MAGIC   | summarize Real_time_protection=dcount(SourceComputerId) by ProtectionStatus, OSName, TypeofProtection
# MAGIC   | where ProtectionStatus == "Real time protection" 
# MAGIC   | project OSName, Real_time_protection)
# MAGIC | union (
# MAGIC   ProtectionStatus
# MAGIC   | where TimeGenerated > ago(100d)
# MAGIC   | summarize Unprotected=dcount(SourceComputerId) by ProtectionStatus, OSName, TypeofProtection
# MAGIC   | where ProtectionStatus == "Unprotected / Unknown" 
# MAGIC   | project OSName, Unprotected)
# MAGIC ```

# COMMAND ----------

# MAGIC %sql
# MAGIC select ProtectionStatus, OSName, count(*) as Count
# MAGIC from protectionstatus
# MAGIC group by ProtectionStatus, OSName

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ##### Considerazioni
# MAGIC 
# MAGIC     Il grafico mostra l’ecosistema di dispositivi presenta un buon livello di configurazione e aggiornamento sul lato server. 
# MAGIC     Lato endpoint invece sono presenti più dispositivi non protetti che possono presentare vulnerabilità che aumentano, per un utente malintenzionato, la superficie di attacco.
# MAGIC     
# MAGIC     Una soluzione potrebbe essere rendere più rigide le policies aziendali riguardo al patching (aggiornamento) dei dispositivi
# MAGIC 
# MAGIC ***

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### Fine
# MAGIC 
# MAGIC Grazie a tutti dell'attenzione.
# MAGIC 
# MAGIC ![Horizon logo](assets/logo_horizon.png "Horizon Security s.r.l.")
