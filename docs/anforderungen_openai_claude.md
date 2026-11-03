# Rekonstruierte Anforderungen an Qrisp

Abgeleitete Leseansicht der Modellausgaben. Maßgeblich bleiben die JSONL-Dateien unter `data/processed/`; Prüfsummen unten. Wörtliche Belegzitate aus den Pull Requests sind bewusst weggelassen (Texte Dritter, vgl. thesis.pdf, Abschnitt 5.1, S. 42). Jeder Pull Request ist stattdessen verlinkt.

Spalten: Satz der Anforderung, EARS-Muster, Typ, Sicherheitsbezug und Belegstärke, jeweils so, wie das Modell sie ausgegeben hat. Der Belegstatus nach G1 und die Bewertung von Hand sind nicht enthalten.

## Inhalt

- [Teil 1: OpenAI gpt-5.6-terra (Volllauf)](#teil-1-openai-gpt-56-terra-volllauf)
- [Teil 2: Anthropic claude-sonnet-5-5 (Vergleichslauf)](#teil-2-anthropic-claude-sonnet-5-5-vergleichslauf)

## Teil 1: OpenAI gpt-5.6-terra (Volllauf)

Volllauf vom 25./26. September 2026 über alle 395 Vorgänge (thesis.pdf, Abschnitt 5.4.3, S. 48). Die Arbeit zählt 1 467 Anforderungen aus 392 schemagültigen Antworten (Abschnitt 6.2.2, Tabelle 6.2, S. 58).

| Angabe | Wert |
|---|---|
| Modell (Manifest) | `gpt-5.6-terra` |
| Quelldatei | `data/processed/extraction_2026-09-25_full_v2.jsonl` |
| SHA-256 der Quelldatei | `3dbc74b24438cac24feba080eca69ef66a4b495b4f7fd677de0f22d7d91e569d` |
| Code-Commit des Laufs | `f9eef00d79c9ae15a2cd76f54ea58372ef62b390` |
| Antworten / davon schemagültig | 395 / 392 |
| Pull Requests mit Anforderungen | 373 |
| Anforderungen (schemagültige Antworten) | 1467 |
| davon sicherheitsrelevant (Modellangabe) | 11 |
| Typ: Schnittstelle | 708 |
| Typ: funktional/Leistung | 581 |
| Typ: Prozess | 148 |
| Typ: Qualität (nicht funktional) | 20 |
| Typ: Gebrauchstauglichkeit | 10 |

### Anforderungen je Pull Request

#### PR 11

[github.com/eclipse-qrisp/Qrisp/pull/11](https://github.com/eclipse-qrisp/Qrisp/pull/11) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0011-01 | The QuantumCircuit.to_pytket method shall convert a given QuantumCircuit to a pytket Circuit. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 13

[github.com/eclipse-qrisp/Qrisp/pull/13](https://github.com/eclipse-qrisp/Qrisp/pull/13) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0013-01 | The requirements shall specify qiskit-ibm-runtime as the Qiskit IBM Runtime dependency. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 14

[github.com/eclipse-qrisp/Qrisp/pull/14](https://github.com/eclipse-qrisp/Qrisp/pull/14) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0014-01 | The QUBO tutorial shall state the QUBO cost operator as the product of the R_{Z_iZ_j}, R_{Z_i}, and global-phase factors. | ubiquitous | Prozess | nein | indirect |

#### PR 29

[github.com/eclipse-qrisp/Qrisp/pull/29](https://github.com/eclipse-qrisp/Qrisp/pull/29) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0029-01 | solve_QUBO shall return the optimal solution as a tuple containing the cost and the optimal bitstring. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0029-02 | solve_QUBO shall use the max_iter argument to set the maximal iteration count of the COBYLA optimizer. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0029-03 | solve_QUBO shall default print_res to False. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 31

[github.com/eclipse-qrisp/Qrisp/pull/31](https://github.com/eclipse-qrisp/Qrisp/pull/31) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0031-01 | When cl_accept(path) evaluates to true, find_solution shall return the input path. | event_driven | funktional/Leistung | nein | indirect |
| QR-0031-02 | When a solution is not obtained with the first QPE result, find_solution shall find a solution. | event_driven | funktional/Leistung | nein | indirect |

#### PR 33

[github.com/eclipse-qrisp/Qrisp/pull/33](https://github.com/eclipse-qrisp/Qrisp/pull/33) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0033-01 | The setup.py shall constrain the Qiskit dependency to versions not greater than 0.44.0. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 34

[github.com/eclipse-qrisp/Qrisp/pull/34](https://github.com/eclipse-qrisp/Qrisp/pull/34) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0034-01 | When adaptive_control_function checks whether a function supports the ctrl_method keyword argument, adaptive_control_function shall inspect the function's full argument specification. | event_driven | funktional/Leistung | nein | indirect |

#### PR 35

[github.com/eclipse-qrisp/Qrisp/pull/35](https://github.com/eclipse-qrisp/Qrisp/pull/35) · 7 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0035-01 | When QAOA parameter optimization completes for a reduced problem, QIROProblem shall reduce the problem again using the replacement routine. | event_driven | funktional/Leistung | nein | indirect |
| QR-0035-02 | When a specific number of recursions has completed, QIROProblem shall return an optimized-solution dictionary for the initial full problem instance. | event_driven | Schnittstelle | nein | indirect |
| QR-0035-03 | qiro_RXMixer shall apply RX rotations to qubit indices absent from the union of its solutions and exclusions lists. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0035-04 | qiro_init_function shall apply Hadamard gates to qubit indices absent from the union of its solutions and exclusions lists. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0035-05 | qiro_init_function shall apply X gates to qubit indices listed in its solutions argument. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0035-06 | When maxSatCostOp receives a problem argument, maxSatCostOp shall use the problem argument’s second element as the clauses. | event_driven | Schnittstelle | nein | indirect |
| QR-0035-07 | When clausesdecoder receives a problem argument, clausesdecoder shall use the argument’s first element as the variable count. | event_driven | Schnittstelle | nein | indirect |

#### PR 37

[github.com/eclipse-qrisp/Qrisp/pull/37](https://github.com/eclipse-qrisp/Qrisp/pull/37) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0037-01 | QIROProblem shall provide a run_qiro operation that accepts a QuantumVariable, QAOA depth, and number of QIRO update steps. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0037-02 | QIROProblem shall optimize the reduced problem with a new QAOAProblem instance. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0037-03 | qrisp.qiro shall provide a QIRO implementation for MaxClique optimization. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0037-04 | qrisp.qiro shall provide a QIRO implementation for MaxIndependentSet optimization. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0037-05 | qrisp.qiro shall provide a QIRO implementation for MaxSat optimization. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0037-06 | qrisp.qiro shall provide a QIRO implementation for MaxSetPacking optimization. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 38

[github.com/eclipse-qrisp/Qrisp/pull/38](https://github.com/eclipse-qrisp/Qrisp/pull/38) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0038-01 | When set_callback is called, QAOAProblem shall enable callback recording. | event_driven | Schnittstelle | nein | indirect |
| QR-0038-02 | While callback recording is enabled, when QAOAProblem computes a classical cost, QAOAProblem shall append the cost to optimization_cost. | complex | funktional/Leistung | nein | indirect |
| QR-0038-03 | When optimization_CB receives a parameter vector, QAOAProblem shall append the parameter vector to optimization_params. | event_driven | funktional/Leistung | nein | indirect |
| QR-0038-04 | While callback recording is enabled, QAOAProblem shall visualize optimization costs against selected gamma and beta parameters. | state_driven | funktional/Leistung | nein | indirect |
| QR-0038-05 | If visualize_cost is called while callback recording is disabled, then QAOAProblem shall raise an exception. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0038-06 | If a selected layer index exceeds the instance depth, then QAOAProblem shall raise an exception. | unwanted_behaviour | Schnittstelle | nein | indirect |

#### PR 39

[github.com/eclipse-qrisp/Qrisp/pull/39](https://github.com/eclipse-qrisp/Qrisp/pull/39) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0039-01 | When callback collection is enabled, QAOAProblem shall append evaluated classical cost values to optimization_cost. | event_driven | funktional/Leistung | nein | indirect |
| QR-0039-02 | When the optimization callback receives a parameter vector, QAOAProblem shall append the vector to optimization_params. | event_driven | funktional/Leistung | nein | indirect |
| QR-0039-03 | If callback collection is disabled, then QAOAProblem shall reject visualize_cost requests. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0039-04 | Where callback collection is enabled, when visualize_cost is invoked, QAOAProblem shall display a scatter plot of selected gamma and beta values colored by optimization costs. | complex | funktional/Leistung | nein | indirect |

#### PR 47

[github.com/eclipse-qrisp/Qrisp/pull/47](https://github.com/eclipse-qrisp/Qrisp/pull/47) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0047-01 | QuantumModulus shall automatically uncompute modular arithmetic operations. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 48

[github.com/eclipse-qrisp/Qrisp/pull/48](https://github.com/eclipse-qrisp/Qrisp/pull/48) · 12 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0048-01 | Qrisp shall translate the `cy` Qrisp gate name to the `CY` Catalyst gate name. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0048-02 | Qrisp shall translate the `cz` Qrisp gate name to the `CZ` Catalyst gate name. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0048-03 | Qrisp shall translate the `crx` Qrisp gate name to the `CRX` Catalyst gate name. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0048-04 | Qrisp shall translate the `crz` Qrisp gate name to the `CRZ` Catalyst gate name. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0048-05 | Qrisp shall translate the `swap` Qrisp gate name to the `SWAP` Catalyst gate name. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0048-06 | Qrisp shall translate the `y` Qrisp gate name to the `PauliY` Catalyst gate name. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0048-07 | Qrisp shall translate the `z` Qrisp gate name to the `PauliZ` Catalyst gate name. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0048-08 | Qrisp shall translate the `rx` Qrisp gate name to the `RX` Catalyst gate name. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0048-09 | Qrisp shall translate the `ry` Qrisp gate name to the `RY` Catalyst gate name. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0048-10 | Qrisp shall translate the `rz` Qrisp gate name to the `RZ` Catalyst gate name. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0048-11 | Qrisp shall translate the `s` Qrisp gate name to the `S` Catalyst gate name. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0048-12 | Qrisp shall translate the `t` Qrisp gate name to the `T` Catalyst gate name. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 51

[github.com/eclipse-qrisp/Qrisp/pull/51](https://github.com/eclipse-qrisp/Qrisp/pull/51) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0051-01 | When invoked with a QuantumVariable in the target Hamming-weight subspace, dicke_state shall prepare an equal superposition of states with the specified Hamming weight. | event_driven | funktional/Leistung | nein | indirect |
| QR-0051-02 | When applied to a portfolio QuantumArray, portfolio_mixer shall preserve the portfolio constraint on lots. | event_driven | funktional/Leistung | nein | indirect |
| QR-0051-03 | When invoked with a portfolio rebalancing problem instance, portfolio_cost_operator shall return a callable cost operator for a QuantumArray. | event_driven | Schnittstelle | nein | indirect |
| QR-0051-04 | When invoked with a portfolio rebalancing problem instance, portfolio_cl_cost_function shall return a callable function that calculates a problem solution's cost value. | event_driven | Schnittstelle | nein | indirect |
| QR-0051-05 | When invoked with a number of lots, portfolio_init shall return a callable function that prepares a QuantumArray initial state for the problem. | event_driven | Schnittstelle | nein | indirect |

#### PR 53

[github.com/eclipse-qrisp/Qrisp/pull/53](https://github.com/eclipse-qrisp/Qrisp/pull/53) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0053-01 | When adding QuantumModulus instances with differing Montgomery shifts, Qrisp shall perform modular in-place addition. | event_driven | funktional/Leistung | nein | indirect |

#### PR 54

[github.com/eclipse-qrisp/Qrisp/pull/54](https://github.com/eclipse-qrisp/Qrisp/pull/54) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0054-01 | The QIROProblem.run_qiro shall accept qarg, depth, n_recursions, mes_kwargs, and max_iter parameters. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0054-02 | The qiro_RXMixer shall respect solutions and exclusions found during QIRO reduction steps. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0054-03 | The qiro_init_function shall respect solutions and exclusions found during QIRO reduction steps. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0054-04 | The Qrisp documentation shall provide a tutorial on Quantum-Informed Recursive Optimization. | ubiquitous | Prozess | nein | indirect |
| QR-0054-05 | The qrisp.qiro.qiroproblems package shall expose the QIRO MaxSat infrastructure. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0054-06 | The qrisp.qiro.qiroproblems package shall expose the QIRO MaxSetPacking infrastructure. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 56

[github.com/eclipse-qrisp/Qrisp/pull/56](https://github.com/eclipse-qrisp/Qrisp/pull/56) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0056-01 | When mod_adder receives an integer addend, mod_adder shall reduce the addend modulo the modulus. | event_driven | funktional/Leistung | nein | indirect |
| QR-0056-02 | When a control is provided, mod_adder shall condition the modular addition on the control. | event_driven | funktional/Leistung | nein | indirect |

#### PR 57

[github.com/eclipse-qrisp/Qrisp/pull/57](https://github.com/eclipse-qrisp/Qrisp/pull/57) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0057-01 | app_sb_phase_polynomial shall apply a phase function specified by a semi-Boolean polynomial to a list of QuantumVariables. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0057-02 | app_phase_polynomial shall apply a phase function specified by a polynomial to a list of QuantumFloats. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0057-03 | If the symbol-list length differs from the total size of the input QuantumVariables, then app_sb_phase_polynomial shall raise an exception. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0057-04 | If the symbol-list length differs from the number of input QuantumFloats, then app_phase_polynomial shall raise an exception. | unwanted_behaviour | Schnittstelle | nein | indirect |

#### PR 58

[github.com/eclipse-qrisp/Qrisp/pull/58](https://github.com/eclipse-qrisp/Qrisp/pull/58) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0058-01 | The create_maxClique_replacement_routine documentation shall describe how correlation-matrix entry selection and sign determine replacement actions. | ubiquitous | Prozess | nein | indirect |
| QR-0058-02 | The create_maxIndep_replacement_routine documentation shall describe how correlation-matrix entry selection and sign determine replacement actions. | ubiquitous | Prozess | nein | indirect |
| QR-0058-03 | The create_maxSat_replacement_routine documentation shall describe how correlation-matrix entry selection and sign determine replacement actions. | ubiquitous | Prozess | nein | indirect |

#### PR 59

[github.com/eclipse-qrisp/Qrisp/pull/59](https://github.com/eclipse-qrisp/Qrisp/pull/59) · 7 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0059-01 | The BackendClient shall include its configured provider name in Qunicorn job data. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0059-02 | The BackendClient shall include its configured device name in Qunicorn job data. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0059-03 | When Qunicorn reports a job state of FINISHED, the BackendClient shall stop polling the job. | event_driven | funktional/Leistung | nein | indirect |
| QR-0059-04 | When processing a Qunicorn COUNTS result, the BackendClient shall return counts with binary-string keys. | event_driven | Schnittstelle | nein | indirect |
| QR-0059-05 | When processing hexadecimal COUNTS results, the BackendClient shall format register segments to the sizes specified in result metadata. | event_driven | funktional/Leistung | nein | indirect |
| QR-0059-06 | If a job response contains no COUNTS result type, then the BackendClient shall raise a ValueError. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0059-07 | If a COUNTS result uses an unknown format, then the BackendClient shall raise a ValueError. | unwanted_behaviour | funktional/Leistung | nein | indirect |

#### PR 64

[github.com/eclipse-qrisp/Qrisp/pull/64](https://github.com/eclipse-qrisp/Qrisp/pull/64) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0064-01 | The BackendClient shall accept a RequestManager as a constructor argument. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0064-02 | When initialization receives a username and password, the RequestManager shall configure its HTTP session with HTTP Basic Authentication credentials. | event_driven | Schnittstelle | **ja** | indirect |
| QR-0064-03 | The RequestManager shall send a GET request to the URL formed by concatenating its base URL with the endpoint. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0064-04 | The RequestManager shall send a POST request to the URL formed by concatenating its base URL with the endpoint. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0064-05 | The RequestManager shall send a DELETE request to the URL formed by concatenating its base URL with the endpoint. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0064-06 | When a RequestManager context exits, the RequestManager shall close its HTTP session. | event_driven | Qualität (nicht funktional) | nein | indirect |

#### PR 65

[github.com/eclipse-qrisp/Qrisp/pull/65](https://github.com/eclipse-qrisp/Qrisp/pull/65) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0065-01 | The Research page shall present papers written by Qrisp developers. | ubiquitous | Prozess | nein | indirect |
| QR-0065-02 | The Research page shall present citations of Qrisp. | ubiquitous | Prozess | nein | indirect |
| QR-0065-03 | The Qrisp documentation shall provide navigation to the Research page. | ubiquitous | Prozess | nein | indirect |

#### PR 66

[github.com/eclipse-qrisp/Qrisp/pull/66](https://github.com/eclipse-qrisp/Qrisp/pull/66) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0066-01 | The Research page shall present research related to Qrisp. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0066-02 | The Research page shall present citations of Qrisp. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 68

[github.com/eclipse-qrisp/Qrisp/pull/68](https://github.com/eclipse-qrisp/Qrisp/pull/68) · 7 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0068-01 | The QAOA reference documentation shall include the QAOAImplemens page. | ubiquitous | Prozess | nein | indirect |
| QR-0068-02 | The QAOA MaxClique documentation shall document the MaxClique QAOA problem. | ubiquitous | Prozess | nein | indirect |
| QR-0068-03 | The QAOA MaxIndependentSet documentation shall document the MaxIndependentSet QAOA problem. | ubiquitous | Prozess | nein | indirect |
| QR-0068-04 | The QAOA MaxSat documentation shall document the MaxSat QAOA problem. | ubiquitous | Prozess | nein | indirect |
| QR-0068-05 | The QAOA MaxSetPacking documentation shall document the MaxSetPacking QAOA problem. | ubiquitous | Prozess | nein | indirect |
| QR-0068-06 | The QAOA MinSetCover documentation shall document the MinSetCover QAOA problem. | ubiquitous | Prozess | nein | indirect |
| QR-0068-07 | The QIROProblem reference documentation shall document the run_qiro method. | ubiquitous | Prozess | nein | indirect |

#### PR 70

[github.com/eclipse-qrisp/Qrisp/pull/70](https://github.com/eclipse-qrisp/Qrisp/pull/70) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0070-01 | When defining the problem graph example, the QAOA tutorial shall invoke nx.erdos_renyi_graph. | event_driven | Schnittstelle | nein | indirect |

#### PR 71

[github.com/eclipse-qrisp/Qrisp/pull/71](https://github.com/eclipse-qrisp/Qrisp/pull/71) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0071-01 | cnot_count shall return the total number of cx, cy, and cz operations in a transpiled circuit. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0071-02 | lightcone_reduction shall reorder a circuit so intended measurements execute as early as possible. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0071-03 | lightcone_reduction shall remove instructions that are not needed for intended measurements. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0071-04 | When an allocated qubit has a first actual instruction, optimize_allocations shall place its allocation gate directly before that instruction. | event_driven | funktional/Leistung | nein | indirect |
| QR-0071-05 | Where a topological-sort function is supplied, PermeabilityGraph shall return a QuantumCircuit ordered by that function. | optional_feature | Schnittstelle | nein | indirect |
| QR-0071-06 | If a cyclic dependency is detected in the uncomputation DAG, then uncompute_qc shall raise an exception. | unwanted_behaviour | funktional/Leistung | nein | indirect |

#### PR 72

[github.com/eclipse-qrisp/Qrisp/pull/72](https://github.com/eclipse-qrisp/Qrisp/pull/72) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0072-01 | When converting hexadecimal data to binary, qunicorn_updates shall produce the correct binary representation. | event_driven | funktional/Leistung | nein | indirect |
| QR-0072-02 | When binding parameters, bind_parameters shall bind the parameters of controlled rotation gates. | event_driven | Schnittstelle | nein | indirect |

#### PR 73

[github.com/eclipse-qrisp/Qrisp/pull/73](https://github.com/eclipse-qrisp/Qrisp/pull/73) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0073-01 | The cl_cost_function shall calculate relative energy using the probability of each measurement sample. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 74

[github.com/eclipse-qrisp/Qrisp/pull/74](https://github.com/eclipse-qrisp/Qrisp/pull/74) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0074-01 | While qv is initialized in the Hamming-weight-k subspace, when dicke_state(qv, k) is called, dicke_state shall prepare an equal superposition of states with Hamming weight k in qv. | complex | funktional/Leistung | nein | indirect |
| QR-0074-02 | Qrisp documentation shall include a reference page for Dicke state preparation. | ubiquitous | Prozess | nein | indirect |
| QR-0074-03 | Qrisp documentation shall include a reference page for HHL. | ubiquitous | Prozess | nein | indirect |

#### PR 77

[github.com/eclipse-qrisp/Qrisp/pull/77](https://github.com/eclipse-qrisp/Qrisp/pull/77) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0077-01 | When evaluating a node, qiro_utils.py shall calculate the node's correlation sum independently of previously evaluated nodes. | event_driven | funktional/Leistung | nein | indirect |

#### PR 78

[github.com/eclipse-qrisp/Qrisp/pull/78](https://github.com/eclipse-qrisp/Qrisp/pull/78) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0078-01 | When invoked with a counts dictionary, time_to_solution shall return the reciprocal of the summed values for bitstrings whose cost equals the optimal solution cost. | event_driven | funktional/Leistung | nein | indirect |

#### PR 84

[github.com/eclipse-qrisp/Qrisp/pull/84](https://github.com/eclipse-qrisp/Qrisp/pull/84) · 8 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0084-01 | Where users install `qrisp[iqm]`, Qrisp shall install qiskit-iqm. | optional_feature | Schnittstelle | nein | indirect |
| QR-0084-02 | Where users want to work with IQM quantum computers as a backend, the README shall instruct users to install `qrisp[iqm]`. | optional_feature | Prozess | nein | indirect |
| QR-0084-03 | The IQMBackend documentation shall include an instantiation example with api_token and device_instance arguments. | ubiquitous | Prozess | nein | indirect |
| QR-0084-04 | If api_token is not a string, then IQMBackend shall raise TypeError. | unwanted_behaviour | Schnittstelle | **ja** | indirect |
| QR-0084-05 | If device_instance is not a string, then IQMBackend shall raise TypeError. | unwanted_behaviour | Schnittstelle | **ja** | indirect |
| QR-0084-06 | If qiskit-iqm cannot be imported, then IQMBackend shall raise ImportError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0084-07 | When callers omit shots, QuantumCircuit.run shall let the backend select the shot count. | event_driven | Schnittstelle | nein | direct |
| QR-0084-08 | When shots is None, IQMBackend shall execute 1000 shots. | event_driven | funktional/Leistung | nein | indirect |

#### PR 86

[github.com/eclipse-qrisp/Qrisp/pull/86](https://github.com/eclipse-qrisp/Qrisp/pull/86) · 7 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0086-01 | IQMBackend shall execute Qrisp programs on IQM quantum computers via IQM Resonance. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0086-02 | Where IQM quantum computers are used as a backend, qrisp[iqm] shall declare qiskit-iqm as a dependency. | optional_feature | Schnittstelle | nein | indirect |
| QR-0086-03 | If api_token is not a string, then IQMBackend shall raise TypeError. | unwanted_behaviour | Schnittstelle | **ja** | indirect |
| QR-0086-04 | If device_instance is not a string, then IQMBackend shall raise TypeError. | unwanted_behaviour | Schnittstelle | **ja** | indirect |
| QR-0086-05 | When QuantumVariable.get_measurement is called without a shot count, QuantumVariable shall use the default shot count of its backend. | event_driven | Schnittstelle | nein | indirect |
| QR-0086-06 | When IQMBackend runs a circuit without a shot count, IQMBackend shall use 1000 shots. | event_driven | funktional/Leistung | nein | indirect |
| QR-0086-07 | When VirtualQiskitBackend is invoked, VirtualQiskitBackend shall issue a deprecation warning recommending QiskitBackend. | event_driven | Schnittstelle | nein | indirect |

#### PR 87

[github.com/eclipse-qrisp/Qrisp/pull/87](https://github.com/eclipse-qrisp/Qrisp/pull/87) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0087-01 | When the IQM Resonance integration is included, the qrisp package shall declare version 0.4.13 for pip. | event_driven | Schnittstelle | nein | indirect |

#### PR 88

[github.com/eclipse-qrisp/Qrisp/pull/88](https://github.com/eclipse-qrisp/Qrisp/pull/88) · 11 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0088-01 | QAOAProblem shall support a TQA warm start. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0088-02 | controlled_RX_mixer_gen shall provide a controlled RX mixer generator. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0088-03 | The QAOA module shall provide a MaxIndepSet QAOA problem instance. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0088-04 | The QAOA module shall provide a MaxClique QAOA problem instance. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0088-05 | The QAOA module shall provide a MaxSetPacking QAOA problem instance. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0088-06 | The QAOA module shall provide a MinSetCover QAOA problem instance. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0088-07 | The QAOA module shall provide a MaxSat QAOA problem instance. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0088-08 | The QAOA module shall provide an E3Lin2 QAOA problem instance. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0088-09 | The QAOA module shall provide a QUBO QAOA problem instance. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0088-10 | solve_QUBO shall solve QUBO problems represented by upper-triangular matrices. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0088-11 | solve_QUBO shall solve QUBO problems represented by symmetrized matrices. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 89

[github.com/eclipse-qrisp/Qrisp/pull/89](https://github.com/eclipse-qrisp/Qrisp/pull/89) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0089-01 | The XY_mixer shall close the qubit interaction ring independently of qubit-count parity. | ubiquitous | funktional/Leistung | nein | direct |

#### PR 90

[github.com/eclipse-qrisp/Qrisp/pull/90](https://github.com/eclipse-qrisp/Qrisp/pull/90) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0090-01 | QIROProblem shall perform QIRO replacement operations on a copy of the networkx graph provided to the instance. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0090-02 | create_maxsat_cost_operator shall accept a MaxSat problem represented by `(num_vars, clauses)`. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0090-03 | create_maxsat_cl_cost_function shall accept a MaxSat problem represented by `(num_vars, clauses)`. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0090-04 | When the maximum-absolute correlation-matrix entry Mii is nonnegative, create_maxsat_replacement_routine shall set value i to true. | event_driven | funktional/Leistung | nein | indirect |
| QR-0090-05 | transform_max_set_pack_to_mis shall represent a MaxSetPacking instance as a constraint graph with subset vertices and intersecting-pair edges. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 91

[github.com/eclipse-qrisp/Qrisp/pull/91](https://github.com/eclipse-qrisp/Qrisp/pull/91) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0091-01 | When the case argument is in superposition, qswitch shall execute the in-place function associated with each case value on operand. | event_driven | funktional/Leistung | nein | indirect |
| QR-0091-02 | When invoked with method set to "parallel", qswitch shall use logarithmic circuit depth. | event_driven | funktional/Leistung | nein | indirect |
| QR-0091-03 | Qrisp shall expose qswitch through its top-level import interface. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 92

[github.com/eclipse-qrisp/Qrisp/pull/92](https://github.com/eclipse-qrisp/Qrisp/pull/92) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0092-01 | If max_item is None, then create_max_clique_replacement_routine shall return (graph, solutions, 0, exclusions). | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0092-02 | When callers omit the solutions and exclusions arguments, create_max_clique_replacement_routine shall initialize them as empty lists. | event_driven | Schnittstelle | nein | indirect |
| QR-0092-03 | If max_item is None, then create_max_indep_replacement_routine shall return (graph, solutions, 0, exclusions). | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0092-04 | When callers omit the solutions and exclusions arguments, create_max_indep_replacement_routine shall initialize them as empty lists. | event_driven | Schnittstelle | nein | indirect |
| QR-0092-05 | If max_item is None, then create_maxsat_replacement_routine shall return (problem, solutions, 0, exclusions). | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0092-06 | When callers omit the solutions and exclusions arguments, create_maxsat_replacement_routine shall initialize them as empty lists. | event_driven | Schnittstelle | nein | indirect |

#### PR 94

[github.com/eclipse-qrisp/Qrisp/pull/94](https://github.com/eclipse-qrisp/Qrisp/pull/94) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0094-01 | While no backend is supplied, the Qiskit backend shall use an AerSimulator instance as its default backend. | state_driven | Schnittstelle | nein | indirect |

#### PR 95

[github.com/eclipse-qrisp/Qrisp/pull/95](https://github.com/eclipse-qrisp/Qrisp/pull/95) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0095-01 | Where callers omit solutions and exclusions, create_max_clique_replacement_routine shall accept the call. | optional_feature | Schnittstelle | nein | indirect |
| QR-0095-02 | If no maximum item is found, then create_max_clique_replacement_routine shall return graph, solutions, zero, and exclusions. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0095-03 | Where callers omit solutions and exclusions, create_max_indep_replacement_routine shall accept the call. | optional_feature | Schnittstelle | nein | indirect |
| QR-0095-04 | If no maximum item is found, then create_max_indep_replacement_routine shall return graph, solutions, zero, and exclusions. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0095-05 | Where callers omit solutions and exclusions, create_maxsat_replacement_routine shall accept the call. | optional_feature | Schnittstelle | nein | indirect |
| QR-0095-06 | If no maximum item is found, then create_maxsat_replacement_routine shall return problem, solutions, zero, and exclusions. | unwanted_behaviour | funktional/Leistung | nein | indirect |

#### PR 96

[github.com/eclipse-qrisp/Qrisp/pull/96](https://github.com/eclipse-qrisp/Qrisp/pull/96) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0096-01 | When a QIRO recursion produces an updated problem state, QIROProblem shall supply the updated problem, solutions, and exclusions to its cost-operator factory. | event_driven | Schnittstelle | nein | indirect |
| QR-0096-02 | When a QIRO recursion produces an updated problem state, QIROProblem shall supply the updated problem, solutions, and exclusions to its mixer factory. | event_driven | Schnittstelle | nein | indirect |
| QR-0096-03 | When an index is absent from the solution and exclusion updates, qiro_rx_mixer shall apply an RX gate to the index. | event_driven | funktional/Leistung | nein | indirect |
| QR-0096-04 | While an index is absent from the union argument, when the predicate is satisfied for that index, qiro_controlled_RX_mixer_gen shall apply an RX gate with parameter beta to the index. | complex | funktional/Leistung | nein | indirect |
| QR-0096-05 | When a MaxSat cost polynomial is nonconstant, create_maxsat_cost_operator_reduced shall return a cost operator that applies its phase polynomial. | event_driven | funktional/Leistung | nein | indirect |
| QR-0096-06 | When initializing a controlled-mixer QIRO maximum-independent-set instance, qiro_max_indep_set_init_function shall apply X gates to solution indices. | event_driven | funktional/Leistung | nein | indirect |

#### PR 97

[github.com/eclipse-qrisp/Qrisp/pull/97](https://github.com/eclipse-qrisp/Qrisp/pull/97) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0097-01 | The memory management algorithm shall execute its topological-sort helper as Numba-compiled code. | ubiquitous | Qualität (nicht funktional) | nein | indirect |
| QR-0097-02 | When no delay function is supplied, delay shall return True when invoked. | event_driven | funktional/Leistung | nein | indirect |
| QR-0097-03 | During a q_int_mult loop iteration indexed by i, q_int_mult shall pass the first len(s)-i elements of factor_2 to inpl_adder. | state_driven | Schnittstelle | nein | insufficient |

#### PR 98

[github.com/eclipse-qrisp/Qrisp/pull/98](https://github.com/eclipse-qrisp/Qrisp/pull/98) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0098-01 | The measurement functions shall measure ladder operators. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0098-02 | QubitOperator shall provide a to_pauli operation that returns an equivalent operator containing only Pauli factors. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0098-03 | QubitOperator shall provide an adjoint operation that returns the adjoint operator. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0098-04 | QubitOperator shall provide a hermitize operation that returns its Hermitian part. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 99

[github.com/eclipse-qrisp/Qrisp/pull/99](https://github.com/eclipse-qrisp/Qrisp/pull/99) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0099-01 | When half of available virtual memory is less than the square of node_amount, toposort_helper shall compute the topological sort without allocating a dense ancestor matrix. | event_driven | funktional/Leistung | nein | indirect |

#### PR 100

[github.com/eclipse-qrisp/Qrisp/pull/100](https://github.com/eclipse-qrisp/Qrisp/pull/100) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0100-01 | When a QIRO recursion updates the problem, QIROProblem shall configure its QIRO operators from the reduced problem state. | event_driven | Schnittstelle | nein | indirect |
| QR-0100-02 | While QIRO reduction solutions or exclusions are present, qiro_rx_mixer shall apply RX rotations only to qubits outside their union. | state_driven | funktional/Leistung | nein | indirect |
| QR-0100-03 | While a QIRO MIS node is absent from the union, when its predicate is satisfied, qiro_controlled_RX_mixer_gen shall apply an RX rotation to the node. | complex | funktional/Leistung | nein | indirect |
| QR-0100-04 | While the controlled-mixer MIS approach has identified solution qubits, qiro_max_indep_set_init_function shall flip the identified solution qubits. | state_driven | funktional/Leistung | nein | indirect |
| QR-0100-05 | When given a reduced MaxSat problem, create_maxsat_cost_operator_reduced shall apply phase-polynomial cost operations for its nonconstant cost polynomials. | event_driven | funktional/Leistung | nein | indirect |
| QR-0100-06 | When a negative single-node correlation is selected, create_max_indep_replacement_routine shall remove the selected node's adjacent nodes from the graph. | event_driven | funktional/Leistung | nein | indirect |

#### PR 101

[github.com/eclipse-qrisp/Qrisp/pull/101](https://github.com/eclipse-qrisp/Qrisp/pull/101) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0101-01 | While QIRO update lists identify solution or exclusion qubits, qiro_rx_mixer shall apply RX gates only to qubits outside their union. | state_driven | funktional/Leistung | nein | indirect |
| QR-0101-02 | While a node is outside the QIRO union, when its predicate is satisfied, qiro_controlled_RX_mixer_gen shall apply an RX gate to the node. | complex | funktional/Leistung | nein | indirect |
| QR-0101-03 | When a QIRO recursion updates the problem, QIROProblem shall construct its cost operator from the updated problem, solutions, and exclusions. | event_driven | funktional/Leistung | nein | indirect |
| QR-0101-04 | When find_max returns a single node with a negative sign, create_max_indep_replacement_routine shall add the node to solutions. | event_driven | funktional/Leistung | nein | indirect |
| QR-0101-05 | When calculating QAOA angles, QAOAProblem shall optimize the circuit compiled at the requested depth with optimization_wrapper. | event_driven | funktional/Leistung | nein | indirect |

#### PR 102

[github.com/eclipse-qrisp/Qrisp/pull/102](https://github.com/eclipse-qrisp/Qrisp/pull/102) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0102-01 | QAOAProblem shall omit the Fourier parameter initialization routine. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 112

[github.com/eclipse-qrisp/Qrisp/pull/112](https://github.com/eclipse-qrisp/Qrisp/pull/112) · 8 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0112-01 | When run receives a quantum circuit, BackendClient shall add the circuit to its internal batch. | event_driven | funktional/Leistung | nein | indirect |
| QR-0112-02 | When its circuit batch reaches batch_size, BackendClient shall dispatch the batch for execution. | event_driven | funktional/Leistung | nein | indirect |
| QR-0112-03 | If its circuit batch has not reached batch_size, then BackendClient shall return None. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0112-04 | If its circuit batch has not reached batch_size, then BackendClient shall generate a debug log. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0112-05 | If dispatch receives an empty circuit batch, then BackendClient shall raise ValueError. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0112-06 | When measurementValue is COUNTS, BackendClient shall return occurrence counts as measurement results. | event_driven | Schnittstelle | nein | indirect |
| QR-0112-07 | When measurementValue is PROBS, BackendClient shall return measurement-outcome probabilities. | event_driven | Schnittstelle | nein | indirect |
| QR-0112-08 | If measurementValue is neither COUNTS nor PROBS, then BackendClient shall raise AttributeError. | unwanted_behaviour | Schnittstelle | nein | indirect |

#### PR 127

[github.com/eclipse-qrisp/Qrisp/pull/127](https://github.com/eclipse-qrisp/Qrisp/pull/127) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0127-01 | The MaxCut tutorial shall construct the condensed QAOA example's problem instance with maxcut_problem(G). | ubiquitous | Prozess | nein | indirect |
| QR-0127-02 | When calculating a best cut in the condensed QAOA example, the MaxCut tutorial shall pass the result bit string in reversed order to maxcut_obj. | event_driven | Prozess | nein | indirect |
| QR-0127-03 | The QUBO tutorial shall import QUBO_problem, QUBO_obj from qrisp.qaoa. | ubiquitous | Prozess | nein | indirect |

#### PR 132

[github.com/eclipse-qrisp/Qrisp/pull/132](https://github.com/eclipse-qrisp/Qrisp/pull/132) · 10 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0132-01 | When called as a function, the Jasp interpreter shall execute a Jasp program. | event_driven | funktional/Leistung | nein | indirect |
| QR-0132-02 | The jaspify decorator shall transform a decorated function into a Jaspr. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0132-03 | The jaspify decorator shall call the simulator for a decorated function. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0132-04 | When Catalyst is installed on Mac or Linux, Jasp programs shall compile to QIR. | event_driven | funktional/Leistung | nein | indirect |
| QR-0132-05 | For each calling signature, the qache decorator shall execute a qached function once. | state_driven | funktional/Leistung | nein | indirect |
| QR-0132-06 | When a qached function is called with a different classical or quantum type, the qache decorator shall retrace the function. | event_driven | funktional/Leistung | nein | indirect |
| QR-0132-07 | When jrange receives a dynamic iteration count, the jrange iterator shall execute that number of loop iterations. | event_driven | funktional/Leistung | nein | indirect |
| QR-0132-08 | The RUS decorator shall repeat a trial function until its first returned classical Boolean value is True. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0132-09 | When a function decorated with terminal_sampling returns a QuantumVariable, the terminal_sampling decorator shall sample the distribution at the end of the script. | event_driven | funktional/Leistung | nein | indirect |
| QR-0132-10 | The tutorial index shall list the Jasp tutorial. | ubiquitous | Prozess | nein | indirect |

#### PR 133

[github.com/eclipse-qrisp/Qrisp/pull/133](https://github.com/eclipse-qrisp/Qrisp/pull/133) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0133-01 | When presenting the QIRO RX mixer in code examples, the QIRO tutorial shall use the name `qiro_rx_mixer`. | event_driven | Schnittstelle | nein | indirect |
| QR-0133-02 | When presenting constrained mixer implementation code, the QIRO tutorial shall import qiro_rz_mixer, create_max_indep_controlled_mixer_reduced, and qiro_max_indep_set_init_function from qrisp.algorithms.qiro. | event_driven | Schnittstelle | nein | indirect |

#### PR 134

[github.com/eclipse-qrisp/Qrisp/pull/134](https://github.com/eclipse-qrisp/Qrisp/pull/134) · 11 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0134-01 | Jasp shall make Qrisp syntax Jax-traceable. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0134-02 | Jasp shall compile Jasp programs to QIR. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0134-03 | When a qache-decorated function is called with the same signature, the qache decorator shall retrieve the appropriate implementation from cache. | event_driven | funktional/Leistung | nein | indirect |
| QR-0134-04 | When a qache-decorated function is called with a different classical or quantum type, the qache decorator shall retrace the function. | event_driven | funktional/Leistung | nein | indirect |
| QR-0134-05 | If a QuantumVariable is injected into a QuantumVariable of a different size, then the injection operator shall raise an error. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0134-06 | The mcx function shall accept a Qubit as a target value. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0134-07 | The mcx function shall accept a QuantumBool as a target value. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0134-08 | QuantumFloats shall perform bit shifts through the in-place operators <<= and >>=. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0134-09 | When invoked, QJIT shall compile and run the program via the Lightning simulator. | event_driven | funktional/Leistung | nein | indirect |
| QR-0134-10 | When a Jasp program requires only boolean gates, Boolean Simulation shall compile the program into a series of boolean operations. | event_driven | funktional/Leistung | nein | indirect |
| QR-0134-11 | When a Jasp function contains only Clifford gates, Stim Simulation shall simulate the function using the Stim simulator. | event_driven | funktional/Leistung | nein | indirect |

#### PR 136

[github.com/eclipse-qrisp/Qrisp/pull/136](https://github.com/eclipse-qrisp/Qrisp/pull/136) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0136-01 | Qrisp shall approximate integrals that are not analytically solvable. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0136-02 | The DB-QITE implementation shall prepare ground states of arbitrary Hamiltonians. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0136-03 | The DB-QITE implementation shall systematically improve ground-state approximations. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0136-04 | The Jasp compilation pipeline shall enable real-time computations. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 141

[github.com/eclipse-qrisp/Qrisp/pull/141](https://github.com/eclipse-qrisp/Qrisp/pull/141) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0141-01 | Standard Qrisp shall provide the Khattar conditionally clean-ancillae multi-controlled X method. | ubiquitous | funktional/Leistung | nein | direct |
| QR-0141-02 | Where JAX-compatible Qrisp is used, Qrisp shall provide the Khattar multi-controlled X method. | optional_feature | funktional/Leistung | nein | direct |
| QR-0141-03 | When mcx is invoked using the khattar method for ctrl_state j, mcx shall produce a true target result for a control-register result equal to j. | event_driven | funktional/Leistung | nein | indirect |
| QR-0141-04 | If a control-register result differs from ctrl_state during an mcx invocation using the khattar method, then mcx shall produce a false target result. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0141-05 | The mcx documentation shall describe the khattar method. | ubiquitous | Prozess | nein | direct |
| QR-0141-06 | The Qrisp test suite shall test the khattar mcx method. | ubiquitous | Prozess | nein | direct |

#### PR 143

[github.com/eclipse-qrisp/Qrisp/pull/143](https://github.com/eclipse-qrisp/Qrisp/pull/143) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0143-01 | When a jax.jit-decorated subroutine is purely classical, jaspify shall compile the subroutine to binary. | event_driven | funktional/Leistung | nein | indirect |

#### PR 146

[github.com/eclipse-qrisp/Qrisp/pull/146](https://github.com/eclipse-qrisp/Qrisp/pull/146) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0146-01 | When shots is None, the Simulator shall return measurement outcomes with nonzero probability as probability values. | event_driven | funktional/Leistung | nein | indirect |
| QR-0146-02 | When the Simulator generates samples, the Simulator shall return integer counts for measurement outcomes. | event_driven | funktional/Leistung | nein | indirect |

#### PR 147

[github.com/eclipse-qrisp/Qrisp/pull/147](https://github.com/eclipse-qrisp/Qrisp/pull/147) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0147-01 | When measure is called, QuantumState shall return the sampled measurement result and the resulting quantum state. | event_driven | Schnittstelle | nein | indirect |
| QR-0147-02 | When adding a qubit, BufferedQuantumState shall associate the added qubit with a simulator index. | event_driven | funktional/Leistung | nein | indirect |
| QR-0147-03 | If a buffered instruction is qb_dealloc, then BufferedQuantumState shall remove the instruction's qubit from its qubit-to-index association. | unwanted_behaviour | funktional/Leistung | nein | indirect |

#### PR 148

[github.com/eclipse-qrisp/Qrisp/pull/148](https://github.com/eclipse-qrisp/Qrisp/pull/148) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0148-01 | When sampling results are requested as an array, the terminal_sampling_interpreter shall return each sampled outcome in the array as many times as its sampled count. | event_driven | funktional/Leistung | nein | insufficient |

#### PR 149

[github.com/eclipse-qrisp/Qrisp/pull/149](https://github.com/eclipse-qrisp/Qrisp/pull/149) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0149-01 | IQPE shall return the estimated phase as a fraction of 2π. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0149-02 | When precision is dynamic, IQPE shall execute its iteration loop dynamically. | event_driven | funktional/Leistung | nein | direct |
| QR-0149-03 | IQPE shall trace U a constant number of times with respect to precision. | ubiquitous | funktional/Leistung | nein | direct |
| QR-0149-04 | When iter_spec is True, IQPE shall call U with an iter keyword argument. | event_driven | Schnittstelle | nein | indirect |

#### PR 150

[github.com/eclipse-qrisp/Qrisp/pull/150](https://github.com/eclipse-qrisp/Qrisp/pull/150) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0150-01 | The qrisp.algorithms.vqe.problems module shall be importable as a Python module. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 151

[github.com/eclipse-qrisp/Qrisp/pull/151](https://github.com/eclipse-qrisp/Qrisp/pull/151) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0151-01 | When mcp is invoked with method="khattar", the mcp function shall apply phase phi according to ctrl_state. | event_driven | Schnittstelle | nein | indirect |
| QR-0151-02 | When mcx is invoked with method="balauca", the mcx function shall preserve the output phase. | event_driven | funktional/Leistung | nein | indirect |

#### PR 152

[github.com/eclipse-qrisp/Qrisp/pull/152](https://github.com/eclipse-qrisp/Qrisp/pull/152) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0152-01 | The QuantumArray array-restructuring methods shall return views without allocating additional qubits. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0152-02 | Where Jasp is used, the QuantumArray shall support runtime indexing. | optional_feature | Schnittstelle | nein | indirect |
| QR-0152-03 | Where Jasp is used, the QuantumArray shall return measured values through measure. | optional_feature | Schnittstelle | nein | indirect |
| QR-0152-04 | When QuantumString.quantize_string is called with a string, QuantumString shall return a QuantumString initialized with the string's characters. | event_driven | Schnittstelle | nein | indirect |

#### PR 154

[github.com/eclipse-qrisp/Qrisp/pull/154](https://github.com/eclipse-qrisp/Qrisp/pull/154) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0154-01 | When catalyst_eqn_evaluator evaluates a jasp.quantum_kernel primitive, catalyst_eqn_evaluator shall insert a 25-qubit quantum register into the output values. | event_driven | Schnittstelle | nein | insufficient |
| QR-0154-02 | ensure_conversion shall convert an input Jaxpr to a Catalyst Jaxpr. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0154-03 | When process_while binds while_p, process_while shall use the while equation's condition-constant count. | event_driven | Schnittstelle | nein | indirect |
| QR-0154-04 | When process_while binds while_p, process_while shall use the while equation's body-constant count. | event_driven | Schnittstelle | nein | indirect |

#### PR 155

[github.com/eclipse-qrisp/Qrisp/pull/155](https://github.com/eclipse-qrisp/Qrisp/pull/155) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0155-01 | trotterization shall provide an optional order parameter with a default value of 1. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0155-02 | Where order is 1, trotterization shall apply the first-order Trotterization formula. | optional_feature | funktional/Leistung | nein | indirect |
| QR-0155-03 | Where order is 2, trotterization shall apply the second-order Trotter-Suzuki formula. | optional_feature | funktional/Leistung | nein | indirect |

#### PR 158

[github.com/eclipse-qrisp/Qrisp/pull/158](https://github.com/eclipse-qrisp/Qrisp/pull/158) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0158-01 | Jaspr shall place the quantum circuit in the last position of its argument signature. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0158-02 | Jaspr shall place the quantum circuit in the last position of its return signature. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0158-03 | The documented frontend shall remain unchanged. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 166

[github.com/eclipse-qrisp/Qrisp/pull/166](https://github.com/eclipse-qrisp/Qrisp/pull/166) · 8 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0166-01 | QubitOperator.expectation_value shall estimate a Hamiltonian expectation value for a state returned by a preparation function. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0166-02 | FermionicOperator.expectation_value shall estimate a Hamiltonian expectation value for a state returned by a preparation function. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0166-03 | When the state-preparation function takes arguments, FermionicOperator.expectation_value shall accept classical values for those arguments. | event_driven | Schnittstelle | nein | indirect |
| QR-0166-04 | The VQE run function shall take a callable qarg_prep as its first argument. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0166-05 | The VQE train function shall take a callable qarg_prep as its first argument. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0166-06 | The VQE benchmark method shall take a callable qarg_prep as its first argument. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0166-07 | When method is 'SPSA', minimize shall execute SPSA minimization. | event_driven | funktional/Leistung | nein | indirect |
| QR-0166-08 | When called, FermionicOperator.get_measurement shall issue a deprecation warning that directs users to .expectation_value. | event_driven | Schnittstelle | nein | indirect |

#### PR 168

[github.com/eclipse-qrisp/Qrisp/pull/168](https://github.com/eclipse-qrisp/Qrisp/pull/168) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0168-01 | When a count_ops-decorated Jasp-compatible function without QuantumKernels is invoked, count_ops shall return a dictionary containing operation counts. | event_driven | Schnittstelle | nein | indirect |
| QR-0168-02 | If profiling_eqn_evaluator encounters the jasp.quantum_kernel primitive, then profiling_eqn_evaluator shall raise an exception indicating that resource estimation cannot be performed. | unwanted_behaviour | funktional/Leistung | nein | indirect |

#### PR 169

[github.com/eclipse-qrisp/Qrisp/pull/169](https://github.com/eclipse-qrisp/Qrisp/pull/169) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0169-01 | When invoked with method="tree", qswitch shall implement a symmetric binary-tree quantum switch. | event_driven | Schnittstelle | nein | indirect |

#### PR 170

[github.com/eclipse-qrisp/Qrisp/pull/170](https://github.com/eclipse-qrisp/Qrisp/pull/170) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0170-01 | When QuantumVariable.template is called, QuantumVariable shall return a QuantumVariableTemplate. | event_driven | Schnittstelle | nein | indirect |
| QR-0170-02 | Where a QuantumVariableTemplate tracks a size, when QuantumVariableTemplate.construct is called without a register, QuantumVariableTemplate shall register a duplicate QuantumVariable with the tracked size. | complex | funktional/Leistung | nein | indirect |
| QR-0170-03 | If QuantumVariableTemplate.construct is called without a register for a template lacking a size specification, then QuantumVariableTemplate shall raise an exception. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0170-04 | If construction of a quantum kernel detects a quantum input, then quantum_kernel shall raise an exception. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0170-05 | If construction of a quantum kernel detects a quantum output, then quantum_kernel shall raise an exception. | unwanted_behaviour | Schnittstelle | nein | indirect |

#### PR 171

[github.com/eclipse-qrisp/Qrisp/pull/171](https://github.com/eclipse-qrisp/Qrisp/pull/171) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0171-01 | When its ancilla variable is in index state \|i⟩, inner_LCU shall apply unitary U_i to the input state. | event_driven | funktional/Leistung | nein | indirect |
| QR-0171-02 | inner_LCU shall return an ancilla case indicator and the target quantum variable after the LCU operation. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0171-03 | If unitaries is neither callable nor a list or tuple, then inner_LCU shall raise TypeError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0171-04 | If unitaries is callable and num_unitaries is unspecified, then inner_LCU shall raise ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0171-05 | LCU shall repeatedly apply the LCU operation until its ancilla register is measured in the \|0⟩ state. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 176

[github.com/eclipse-qrisp/Qrisp/pull/176](https://github.com/eclipse-qrisp/Qrisp/pull/176) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0176-01 | When fuse_abstract_eval receives two operands whose types belong to {AbstractQubit, AbstractQubitArray}, fuse_abstract_eval shall return an AbstractQubitArray. | event_driven | Schnittstelle | nein | indirect |
| QR-0176-02 | When fuse_impl receives one list operand and one non-list operand, fuse_impl shall return a list containing the input values in argument order. | event_driven | Schnittstelle | nein | indirect |

#### PR 178

[github.com/eclipse-qrisp/Qrisp/pull/178](https://github.com/eclipse-qrisp/Qrisp/pull/178) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0178-01 | While Jasp tracing mode is active, IQAE shall return an iterative quantum amplitude estimate. | state_driven | funktional/Leistung | nein | indirect |
| QR-0178-02 | While Jasp tracing mode is active, qswitch shall apply the case function selected by the case value. | state_driven | funktional/Leistung | nein | indirect |
| QR-0178-03 | When diffuser receives a tuple input_object and reflection_indices is None, diffuser shall derive reflection indices for the tuple elements. | event_driven | Schnittstelle | nein | indirect |

#### PR 179

[github.com/eclipse-qrisp/Qrisp/pull/179](https://github.com/eclipse-qrisp/Qrisp/pull/179) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0179-01 | While operating in tracing mode, QAOAProblem shall use a JAX-traceable optimization routine. | state_driven | funktional/Leistung | nein | direct |
| QR-0179-02 | While no init_function is specified, when init_type is tqa, QAOAProblem shall prepare the \|−⟩^n state. | complex | funktional/Leistung | nein | indirect |
| QR-0179-03 | The RY_mixer shall apply an RY rotation of 2 * beta to each qubit in the supplied QuantumVariable. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0179-04 | The create_maxcut_sample_array_post_processor shall return the mean cut value for a supplied sample array. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0179-05 | Where terminal_sampling is enabled, the integrated Qrisp simulator shall draw samples from the state vector. | optional_feature | funktional/Leistung | nein | indirect |

#### PR 181

[github.com/eclipse-qrisp/Qrisp/pull/181](https://github.com/eclipse-qrisp/Qrisp/pull/181) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0181-01 | Where case_function is a list of functions, qswitch shall execute the function selected by case on operand. | optional_feature | Schnittstelle | nein | indirect |
| QR-0181-02 | Where case_function is callable, qswitch shall invoke the callable with a nonnegative integer case index and operand. | optional_feature | Schnittstelle | nein | indirect |
| QR-0181-03 | Where method is tree, qswitch shall execute the case function selected by case on operand. | optional_feature | funktional/Leistung | nein | indirect |

#### PR 184

[github.com/eclipse-qrisp/Qrisp/pull/184](https://github.com/eclipse-qrisp/Qrisp/pull/184) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0184-01 | While Jasp tracing mode is active, when `method` is `"tree"` and `case_function_list` is a list, qswitch shall accept `case_function_list`. | complex | Schnittstelle | nein | indirect |
| QR-0184-02 | While Jasp tracing mode is inactive, when `method` is `"tree"` and `case_function_list` is a list, qswitch shall accept `case_function_list`. | complex | Schnittstelle | nein | indirect |
| QR-0184-03 | While Jasp tracing mode is active, when `method` is `"tree"` and `case_function_list` is callable, qswitch shall accept `case_function_list`. | complex | Schnittstelle | nein | indirect |
| QR-0184-04 | While Jasp tracing mode is inactive, when `method` is `"tree"` and `case_function_list` is callable, qswitch shall accept `case_function_list`. | complex | Schnittstelle | nein | indirect |

#### PR 185

[github.com/eclipse-qrisp/Qrisp/pull/185](https://github.com/eclipse-qrisp/Qrisp/pull/185) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0185-01 | When commute_pauli compares two QubitTerms, QubitTerm shall determine whether their Pauli factors commute and their ladder factors commute qubit-wise. | event_driven | Schnittstelle | nein | indirect |
| QR-0185-02 | When QubitOperator measurement uses diagonalisation method 'commuting', QubitOperator shall group terms only when their Pauli factors commute and their ladder factors commute qubit-wise. | event_driven | funktional/Leistung | nein | indirect |
| QR-0185-03 | When QubitOperator trotterization uses method 'commuting', QubitOperator shall group terms only when their Pauli factors commute and their ladder factors commute qubit-wise. | event_driven | funktional/Leistung | nein | indirect |

#### PR 186

[github.com/eclipse-qrisp/Qrisp/pull/186](https://github.com/eclipse-qrisp/Qrisp/pull/186) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0186-01 | When amplitude amplification runs in non-tracing mode with a positive iteration count, amplitude amplification shall apply the specified oracle function followed by the diffuser once per iteration. | event_driven | funktional/Leistung | nein | indirect |
| QR-0186-02 | When Grover's algorithm runs in non-tracing mode, Grover's algorithm shall apply the specified oracle function followed by the diffuser once per iteration. | event_driven | funktional/Leistung | nein | indirect |

#### PR 187

[github.com/eclipse-qrisp/Qrisp/pull/187](https://github.com/eclipse-qrisp/Qrisp/pull/187) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0187-01 | QITE shall be Jasp-compatible for the GC method. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0187-02 | QITE shall be Jasp-compatible for the HOPF method. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 188

[github.com/eclipse-qrisp/Qrisp/pull/188](https://github.com/eclipse-qrisp/Qrisp/pull/188) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0188-01 | When method is COBYLA, minimize shall execute COBYLA optimization. | event_driven | Schnittstelle | nein | indirect |
| QR-0188-02 | minimize shall interpret maxiter as the maximum number of optimization iterations. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 191

[github.com/eclipse-qrisp/Qrisp/pull/191](https://github.com/eclipse-qrisp/Qrisp/pull/191) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0191-01 | The Tutorials page shall present linked tutorial entries. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 193

[github.com/eclipse-qrisp/Qrisp/pull/193](https://github.com/eclipse-qrisp/Qrisp/pull/193) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0193-01 | When its qswitch conjugator invokes mcx, switch_case.py shall use the 'balauca' method. | event_driven | funktional/Leistung | nein | indirect |

#### PR 195

[github.com/eclipse-qrisp/Qrisp/pull/195](https://github.com/eclipse-qrisp/Qrisp/pull/195) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0195-01 | The COBYLA optimizer shall be JASP-compatible. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0195-02 | The jasp.minimize function shall default to the COBYLA optimizer. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 196

[github.com/eclipse-qrisp/Qrisp/pull/196](https://github.com/eclipse-qrisp/Qrisp/pull/196) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0196-01 | When the meas_behavior argument is "0", count_ops shall compute resource counts as though measurements return 0. | event_driven | Schnittstelle | nein | indirect |
| QR-0196-02 | When the meas_behavior argument is "1", count_ops shall compute resource counts as though measurements return 1. | event_driven | Schnittstelle | nein | indirect |
| QR-0196-03 | When the meas_behavior argument is callable, count_ops shall use the callable's Boolean return values as measurement results during resource computation. | event_driven | Schnittstelle | nein | indirect |
| QR-0196-04 | When the meas_behavior argument is "sim", count_ops shall determine measurement behavior using the Qrisp simulator. | event_driven | Schnittstelle | nein | indirect |
| QR-0196-05 | If meas_behavior is a string other than the strings "0", "1", and "sim", then profile_jaspr shall reject the resource computation. | unwanted_behaviour | Schnittstelle | nein | indirect |

#### PR 197

[github.com/eclipse-qrisp/Qrisp/pull/197](https://github.com/eclipse-qrisp/Qrisp/pull/197) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0197-01 | REQUIREMENTS shall declare numpy>=2.0 as a package dependency. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0197-02 | Jasp shall be compatible with the COBYLA Optimizer. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0197-03 | jasp.minimize shall use COBYLA as its default optimizer. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 202

[github.com/eclipse-qrisp/Qrisp/pull/202](https://github.com/eclipse-qrisp/Qrisp/pull/202) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0202-01 | qswitch shall accept a case_amount argument that specifies the number of cases. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0202-02 | Where case_amount is None, when case_function is a single function, qswitch shall infer the number of cases from the size of the case variable. | complex | Schnittstelle | nein | indirect |
| QR-0202-03 | Where case_amount is None, when case_function is a list of functions, qswitch shall infer the number of cases from the length of the list. | complex | Schnittstelle | nein | indirect |
| QR-0202-04 | When the case value is greater than or equal to case_amount, qswitch shall leave the operand unchanged. | event_driven | funktional/Leistung | nein | indirect |
| QR-0202-05 | When case_amount is not a power of two, qswitch shall terminate tree traversal without visiting cases beyond case_amount. | event_driven | funktional/Leistung | nein | indirect |
| QR-0202-06 | When case_amount differs from the number of values represented by the case variable, qswitch shall issue a warning. | event_driven | funktional/Leistung | nein | indirect |

#### PR 204

[github.com/eclipse-qrisp/Qrisp/pull/204](https://github.com/eclipse-qrisp/Qrisp/pull/204) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0204-01 | The custom_inversion decorator shall allow users to specify customized inversion behavior for decorated functions. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0204-02 | When customized inversion is requested for qswitch, the qswitch function shall execute its case functions under inversion. | event_driven | funktional/Leistung | nein | indirect |

#### PR 205

[github.com/eclipse-qrisp/Qrisp/pull/205](https://github.com/eclipse-qrisp/Qrisp/pull/205) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0205-01 | When a Python integer larger than 64 bits and a limb count are supplied, BigInteger.create_static shall construct a BigInteger from the integer. | event_driven | Schnittstelle | nein | indirect |
| QR-0205-02 | When cq_montgomery_multiply receives a classical X and a QuantumFloat y, cq_montgomery_multiply shall return X*y mod N in standard representation. | event_driven | funktional/Leistung | nein | indirect |
| QR-0205-03 | When qq_montgomery_multiply receives two QuantumFloats in Montgomery form, qq_montgomery_multiply shall return their Montgomery product. | event_driven | funktional/Leistung | nein | indirect |
| QR-0205-04 | When a QuantumArray has a QuantumModulus qtype, QuantumArray shall support matrix multiplication. | event_driven | Schnittstelle | nein | indirect |
| QR-0205-05 | When tracing mode is active, modinv shall return the modular inverse. | event_driven | funktional/Leistung | nein | indirect |
| QR-0205-06 | The Scalable Integer Type documentation shall include an example demonstrating BigInteger with QuantumModulus. | ubiquitous | Prozess | nein | direct |

#### PR 209

[github.com/eclipse-qrisp/Qrisp/pull/209](https://github.com/eclipse-qrisp/Qrisp/pull/209) · 7 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0209-01 | If unitaries is neither callable nor a list, then inner_LCU shall raise TypeError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0209-02 | If unitaries is callable and num_unitaries is unspecified, then inner_LCU shall raise ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0209-03 | inner_LCU shall return without measuring the ancilla variable. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0209-04 | inner_LCU shall return the ancilla variable. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0209-05 | inner_LCU shall return the transformed target variable. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0209-06 | If the ancilla measurement does not yield the ket 0 state, then LCU shall rerun the LCU circuit. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0209-07 | view_LCU shall return the explicit quantum circuit corresponding to the LCU protocol. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 214

[github.com/eclipse-qrisp/Qrisp/pull/214](https://github.com/eclipse-qrisp/Qrisp/pull/214) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0214-01 | When encoding a number into a QuantumFloat with more than 63 qubits, the quantum float encoder shall mask the integer encoding to 63 bits. | event_driven | funktional/Leistung | nein | indirect |

#### PR 216

[github.com/eclipse-qrisp/Qrisp/pull/216](https://github.com/eclipse-qrisp/Qrisp/pull/216) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0216-01 | The Qrisp learning module shall include three learning chapters for QC beginners in the HTML build. | ubiquitous | Prozess | nein | indirect |
| QR-0216-02 | When `verify` is set to true, Qrisp shall delete only qubits in the `\|0⟩` state. | event_driven | funktional/Leistung | nein | indirect |
| QR-0216-03 | When the `auto_uncompute` decorator is applied to a function, the auto_uncompute decorator shall uncompute variables used in the function. | event_driven | funktional/Leistung | nein | indirect |
| QR-0216-04 | The QuantumChar shall initialize in NISQ mode by default. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0216-05 | When `nisq_char` is set to `False`, the QuantumChar shall use eight qubits per character. | event_driven | funktional/Leistung | nein | indirect |

#### PR 217

[github.com/eclipse-qrisp/Qrisp/pull/217](https://github.com/eclipse-qrisp/Qrisp/pull/217) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0217-01 | IQMBackend shall accept a compilation_options argument for pulse-level compilation options. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0217-02 | If compilation_options is not provided, then IQMBackend shall create default CircuitCompilationOptions. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0217-03 | When its run function executes, IQMBackend shall submit the circuit using the configured compilation options. | event_driven | funktional/Leistung | nein | indirect |

#### PR 219

[github.com/eclipse-qrisp/Qrisp/pull/219](https://github.com/eclipse-qrisp/Qrisp/pull/219) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0219-01 | The iqm extra shall depend on iqm-client[qiskit]. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0219-02 | When called with phi, theta, and qubits, the r method shall append an RGate to qubits. | event_driven | Schnittstelle | nein | indirect |
| QR-0219-03 | When an operation is named r, the Qiskit converter shall create a Qiskit RGate using the operation parameters. | event_driven | Schnittstelle | nein | insufficient |
| QR-0219-04 | Where the QRISP_SIMULATOR_FLOAT_THRESH environment variable is present, numerics_config shall use its value for float_thresh. | optional_feature | Schnittstelle | nein | insufficient |
| QR-0219-05 | Where the QRISP_SIMULATOR_CUTOFF_RATIO environment variable is present, numerics_config shall use its value for cutoff_ratio. | optional_feature | Schnittstelle | nein | insufficient |
| QR-0219-06 | Where the QRISP_SIMULATOR_SPARSIFICATION_RATE environment variable is present, numerics_config shall use its value for sparsification_rate. | optional_feature | Schnittstelle | nein | insufficient |

#### PR 221

[github.com/eclipse-qrisp/Qrisp/pull/221](https://github.com/eclipse-qrisp/Qrisp/pull/221) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0221-01 | When the QRISP_SIMULATOR_FLOAT_THRESH environment variable is defined, the Qrisp simulator shall use its value as the float threshold. | event_driven | Schnittstelle | nein | indirect |
| QR-0221-02 | When the QRISP_SIMULATOR_CUTOFF_RATIO environment variable is defined, the Qrisp simulator shall use its value as the cutoff ratio. | event_driven | Schnittstelle | nein | indirect |
| QR-0221-03 | When the QRISP_SIMULATOR_SPARSIFICATION_RATE environment variable is defined, the Qrisp simulator shall use its value as the sparsification rate. | event_driven | Schnittstelle | nein | indirect |
| QR-0221-04 | During measurement, the Qrisp simulator shall consider a complex or float value below the float threshold to be zero. | state_driven | funktional/Leistung | nein | indirect |
| QR-0221-05 | When completing a matrix multiplication, the Qrisp simulator shall consider a complex or float value below np.max(np.abs(statevector))*cutoff_ratio to be zero. | event_driven | funktional/Leistung | nein | indirect |
| QR-0221-06 | The Qrisp simulator shall use a sparsification rate from 0 through 1 inclusive. | ubiquitous | funktional/Leistung | nein | direct |

#### PR 225

[github.com/eclipse-qrisp/Qrisp/pull/225](https://github.com/eclipse-qrisp/Qrisp/pull/225) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0225-01 | ladder1_synth_jax shall synthesize a logarithmic-depth CNOT circuit equivalent to a CNOT ladder of length n-1. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0225-02 | ladder2_synth_jax shall synthesize a polylogarithmic-depth MCX circuit equivalent to a Toffoli ladder of length n-1. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0225-03 | remaud_adder shall store the result of adding the two n-bit inputs A and B in B. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0225-04 | remaud_adder shall store the carry bit of adding A and B in Z. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0225-05 | remaud_adder shall leave A invariant. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0225-06 | remaud_adder shall implement addition with polylogarithmic circuit depth. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 227

[github.com/eclipse-qrisp/Qrisp/pull/227](https://github.com/eclipse-qrisp/Qrisp/pull/227) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0227-01 | BatchedBackend shall queue circuit queries submitted through run until dispatch sends their batch for execution. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0227-02 | When dispatch sends a collected batch, BatchedBackend shall resume threads that submitted backend calls in that batch. | event_driven | funktional/Leistung | nein | indirect |
| QR-0227-03 | When BatchedBackend.run is called from the main thread, BatchedBackend shall automatically dispatch pending queries including the main-thread query. | event_driven | funktional/Leistung | nein | indirect |
| QR-0227-04 | batched_measurement shall return a list of measurement results for the supplied QuantumVariables. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0227-05 | IQMBackend shall return a BatchedBackend by default. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0227-06 | Where the backend is a BatchedBackend, get_measurement shall dispatch measurement-operator calls as a batch. | optional_feature | funktional/Leistung | nein | indirect |

#### PR 229

[github.com/eclipse-qrisp/Qrisp/pull/229](https://github.com/eclipse-qrisp/Qrisp/pull/229) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0229-01 | QiskitRuntimeBackend shall configure QiskitRuntimeService with the ibm_quantum_platform channel. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0229-02 | When no backend is supplied, QiskitRuntimeBackend shall select the least busy backend from QiskitRuntimeService. | event_driven | funktional/Leistung | nein | indirect |
| QR-0229-03 | When a backend is supplied, QiskitRuntimeBackend shall resolve the supplied backend through QiskitRuntimeService. | event_driven | Schnittstelle | nein | indirect |
| QR-0229-04 | When executing a QASM string, QiskitRuntimeBackend shall submit a singleton list containing the transpiled circuit to Sampler. | event_driven | Schnittstelle | nein | indirect |

#### PR 230

[github.com/eclipse-qrisp/Qrisp/pull/230](https://github.com/eclipse-qrisp/Qrisp/pull/230) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0230-01 | While R is a positive binary QuantumFloat in 2's complement representation with an even number of bits, isqrt_alg shall return the integer square root of R. | state_driven | Schnittstelle | nein | indirect |
| QR-0230-02 | While R is a positive binary QuantumFloat in 2's complement representation with an even number of bits, isqrt_alg shall transform R into the integer-square-root remainder. | state_driven | funktional/Leistung | nein | indirect |
| QR-0230-03 | The isqrt algorithm shall leave no garbage. | ubiquitous | Qualität (nicht funktional) | nein | indirect |
| QR-0230-04 | The isqrt algorithm shall be T-Count optimized. | ubiquitous | Qualität (nicht funktional) | nein | indirect |

#### PR 231

[github.com/eclipse-qrisp/Qrisp/pull/231](https://github.com/eclipse-qrisp/Qrisp/pull/231) · 9 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0231-01 | When q_isqrt receives a non-negative integer QuantumFloat with zero exponent, q_isqrt shall return its integer square root. | event_driven | funktional/Leistung | nein | indirect |
| QR-0231-02 | When q_isqrt receives a non-negative integer QuantumFloat with zero exponent, q_isqrt shall transform the input QuantumFloat into the remainder of the square-root computation. | event_driven | funktional/Leistung | nein | indirect |
| QR-0231-03 | When q_isqrt receives a QuantumFloat, q_isqrt shall operate without requiring the caller to modify the QuantumFloat size. | event_driven | Schnittstelle | nein | direct |
| QR-0231-04 | When q_isqrt receives a QuantumFloat in a superposition state, q_isqrt shall compute integer-square-root results for the superposed input values. | event_driven | funktional/Leistung | nein | direct |
| QR-0231-05 | When q_isqrt receives a signed QuantumFloat representing a non-negative integer, q_isqrt shall accept the QuantumFloat as input. | event_driven | Schnittstelle | nein | direct |
| QR-0231-06 | When q_isqrt receives an unsigned QuantumFloat representing a non-negative integer, q_isqrt shall accept the QuantumFloat as input. | event_driven | Schnittstelle | nein | direct |
| QR-0231-07 | The q_isqrt documentation shall state that q_isqrt does not yield plausible output for negative integers. | ubiquitous | Prozess | nein | direct |
| QR-0231-08 | If q_isqrt receives a QuantumFloat with a non-zero exponent, then q_isqrt shall raise an exception. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0231-09 | The q_isqrt operation shall leave no garbage qubits after computing the integer square root and remainder. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 237

[github.com/eclipse-qrisp/Qrisp/pull/237](https://github.com/eclipse-qrisp/Qrisp/pull/237) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0237-01 | IQMBackend shall instantiate the IQM client with the supplied server_url. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0237-02 | When a caller omits server_url, IQMBackend shall use the IQM Resonance URL for device_instance. | event_driven | Schnittstelle | nein | indirect |
| QR-0237-03 | If both server_url and device_instance are provided, then IQMBackend shall raise a ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0237-04 | If neither server_url nor device_instance is provided, then IQMBackend shall raise a ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0237-05 | If server_url is provided with a non-string value, then IQMBackend shall raise a TypeError. | unwanted_behaviour | Schnittstelle | nein | indirect |

#### PR 241

[github.com/eclipse-qrisp/Qrisp/pull/241](https://github.com/eclipse-qrisp/Qrisp/pull/241) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0241-01 | When determining the result type for addition of two QuantumFloat operands, QuantumFloat shall set the maximum significand index to one greater than the greater operand maximum significand index. | event_driven | funktional/Leistung | nein | indirect |
| QR-0241-02 | When determining the result type for subtraction of two QuantumFloat operands, QuantumFloat shall set the maximum significand index to one greater than the greater operand maximum significand index. | event_driven | funktional/Leistung | nein | indirect |

#### PR 242

[github.com/eclipse-qrisp/Qrisp/pull/242](https://github.com/eclipse-qrisp/Qrisp/pull/242) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0242-01 | The Jasp high-level interface shall remain compatible with JAX 0.6.0. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0242-02 | Qrisp shall require jax version 0.6.0. | ubiquitous | Schnittstelle | nein | insufficient |
| QR-0242-03 | Qrisp shall require jaxlib version 0.6.0. | ubiquitous | Schnittstelle | nein | insufficient |
| QR-0242-04 | If the QuantumCircuit trace differs from the current JAX trace, then TracingQuantumSession.append shall raise an exception identifying lost QuantumCircuit tracking. | unwanted_behaviour | funktional/Leistung | nein | indirect |

#### PR 245

[github.com/eclipse-qrisp/Qrisp/pull/245](https://github.com/eclipse-qrisp/Qrisp/pull/245) · 8 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0245-01 | QiskitBackend shall submit transpiled circuits through Qiskit SamplerV2. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0245-02 | When no shot count is supplied, QiskitBackend shall execute 1000 shots. | event_driven | funktional/Leistung | nein | indirect |
| QR-0245-03 | QiskitRuntimeBackend shall accept a channel type when it initializes the Qiskit Runtime service. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0245-04 | When initialized without a backend name, QiskitRuntimeBackend shall select the least busy available runtime backend. | event_driven | funktional/Leistung | nein | indirect |
| QR-0245-05 | When initialized with mode "session", QiskitRuntimeBackend shall create a Qiskit Runtime session. | event_driven | funktional/Leistung | nein | indirect |
| QR-0245-06 | When initialized with mode "job", QiskitRuntimeBackend shall create a SamplerV2 for the backend. | event_driven | funktional/Leistung | nein | indirect |
| QR-0245-07 | If initialized with an unsupported execution mode, then QiskitRuntimeBackend shall raise ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0245-08 | When no shot count is supplied, QiskitRuntimeBackend shall execute 1000 shots. | event_driven | funktional/Leistung | nein | indirect |

#### PR 246

[github.com/eclipse-qrisp/Qrisp/pull/246](https://github.com/eclipse-qrisp/Qrisp/pull/246) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0246-01 | The documentation website shall publish tutorial content in Jupyter Notebook format. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0246-02 | When displaying a general/tutorial notebook page, the documentation website shall present a download link to the page's Jupyter Notebook. | event_driven | Schnittstelle | nein | indirect |

#### PR 248

[github.com/eclipse-qrisp/Qrisp/pull/248](https://github.com/eclipse-qrisp/Qrisp/pull/248) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0248-01 | Tutorials shall be notebooks. | ubiquitous | Prozess | nein | indirect |
| QR-0248-02 | When a notebook page is displayed, the Sidebar shall provide a link to download the page's Jupyter Notebook. | event_driven | Schnittstelle | nein | indirect |
| QR-0248-03 | When a specific tutorial is referenced, references to specific tutorials shall link to that tutorial. | event_driven | Schnittstelle | nein | direct |

#### PR 249

[github.com/eclipse-qrisp/Qrisp/pull/249](https://github.com/eclipse-qrisp/Qrisp/pull/249) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0249-01 | Jaspr shall be a subtype of jax.extend.core.ClosedJaxpr. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0249-02 | Jaspr shall associate concrete values with its constant variables. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0249-03 | When Jaspr.from_cache converts a ClosedJaxpr, Jaspr shall retain the ClosedJaxpr concrete constants. | event_driven | Schnittstelle | nein | indirect |

#### PR 253

[github.com/eclipse-qrisp/Qrisp/pull/253](https://github.com/eclipse-qrisp/Qrisp/pull/253) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0253-01 | Thebe shall use input fields for executable cells. | ubiquitous | Schnittstelle | nein | direct |
| QR-0253-02 | When a ThebeLab cell is rendered inside an existing Jupyter notebook box, the ThebeLab cell shall render without a border. | event_driven | Gebrauchstauglichkeit | nein | direct |

#### PR 255

[github.com/eclipse-qrisp/Qrisp/pull/255](https://github.com/eclipse-qrisp/Qrisp/pull/255) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0255-01 | gate_wrap shall preserve the original function signature in documentation. | ubiquitous | Gebrauchstauglichkeit | nein | indirect |

#### PR 256

[github.com/eclipse-qrisp/Qrisp/pull/256](https://github.com/eclipse-qrisp/Qrisp/pull/256) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0256-01 | When called with same-sized a and b operands, remaud_adder shall store (a + b) modulo 2^N in b, where N is their shared size. | event_driven | funktional/Leistung | nein | indirect |
| QR-0256-02 | When called, remaud_adder shall preserve the value of a. | event_driven | funktional/Leistung | nein | indirect |
| QR-0256-03 | When the sum overflows the shared operand size, remaud_adder shall store the carry bit in z. | event_driven | funktional/Leistung | nein | indirect |
| QR-0256-04 | remaud_adder shall execute with polylogarithmic circuit depth. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0256-05 | remaud_adder shall use no auxiliary qubits. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 261

[github.com/eclipse-qrisp/Qrisp/pull/261](https://github.com/eclipse-qrisp/Qrisp/pull/261) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0261-01 | The tests folder shall group tests by module. | ubiquitous | Prozess | nein | indirect |
| QR-0261-02 | When its run function is called from the main thread, the batched backend shall evaluate the backend immediately. | event_driven | funktional/Leistung | nein | indirect |
| QR-0261-03 | When backend evaluation raises an exception, the batched backend shall raise the captured backend-evaluation exception in the main thread. | event_driven | funktional/Leistung | nein | indirect |

#### PR 268

[github.com/eclipse-qrisp/Qrisp/pull/268](https://github.com/eclipse-qrisp/Qrisp/pull/268) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0268-01 | The Grover example documentation shall calculate the iteration count as round(π/(2θ) - 0.5), where θ equals 2 asin(sqrt(M/N)). | ubiquitous | Prozess | nein | indirect |

#### PR 270

[github.com/eclipse-qrisp/Qrisp/pull/270](https://github.com/eclipse-qrisp/Qrisp/pull/270) · 9 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0270-01 | setup.py shall declare webencodings as a dependency. | ubiquitous | Schnittstelle | nein | insufficient |
| QR-0270-02 | setup.py shall declare beautifulsoup4 as a dependency. | ubiquitous | Schnittstelle | nein | insufficient |
| QR-0270-03 | setup.py shall declare tinycss2 as a dependency. | ubiquitous | Schnittstelle | nein | insufficient |
| QR-0270-04 | setup.py shall declare pytest as a dependency. | ubiquitous | Schnittstelle | nein | insufficient |
| QR-0270-05 | setup.py shall declare stim as a dependency. | ubiquitous | Schnittstelle | nein | insufficient |
| QR-0270-06 | setup.py shall declare pennylane-catalyst as a dependency. | ubiquitous | Schnittstelle | nein | insufficient |
| QR-0270-07 | setup.py shall declare qiskit-aer as a dependency. | ubiquitous | Schnittstelle | nein | insufficient |
| QR-0270-08 | setup.py shall declare qiskit-iqm as a dependency. | ubiquitous | Schnittstelle | nein | insufficient |
| QR-0270-09 | setup.py shall declare pyscf as a dependency. | ubiquitous | Schnittstelle | nein | insufficient |

#### PR 272

[github.com/eclipse-qrisp/Qrisp/pull/272](https://github.com/eclipse-qrisp/Qrisp/pull/272) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0272-01 | When qswitch is invoked within a control context, qswitch shall condition selected case-function execution on the context's control qubit. | event_driven | Schnittstelle | nein | indirect |
| QR-0272-02 | If qswitch receives a case-function list with the sequential method and a non-None case_amount, then qswitch shall raise a TypeError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0272-03 | If qswitch receives a case_function that is not a list and is not callable, then qswitch shall raise a TypeError. | unwanted_behaviour | Schnittstelle | nein | indirect |

#### PR 273

[github.com/eclipse-qrisp/Qrisp/pull/273](https://github.com/eclipse-qrisp/Qrisp/pull/273) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0273-01 | When qswitch runs outside Jasp, qswitch shall execute the branch selected by a conditional predicate. | event_driven | funktional/Leistung | nein | indirect |

#### PR 274

[github.com/eclipse-qrisp/Qrisp/pull/274](https://github.com/eclipse-qrisp/Qrisp/pull/274) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0274-01 | When a push targets main, the GitHub workflow shall run tests. | event_driven | Prozess | nein | indirect |
| QR-0274-02 | When a pull request targets main, the GitHub workflow shall run tests. | event_driven | Prozess | nein | indirect |
| QR-0274-03 | When a push occurs, the pipeline shall run. | event_driven | Prozess | nein | direct |

#### PR 275

[github.com/eclipse-qrisp/Qrisp/pull/275](https://github.com/eclipse-qrisp/Qrisp/pull/275) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0275-01 | When Jasp evaluates an equality comparison between QuantumFloats, equal shall yield the equality result. | event_driven | Schnittstelle | nein | indirect |
| QR-0275-02 | When Jasp evaluates a QuantumFloat truncation, QuantumFloat.truncate shall return a representable value obtained by rounding the supplied value. | event_driven | Schnittstelle | nein | indirect |
| QR-0275-03 | QuantumFloat.truncate shall have constant scaling with respect to QuantumFloat size. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 277

[github.com/eclipse-qrisp/Qrisp/pull/277](https://github.com/eclipse-qrisp/Qrisp/pull/277) · 8 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0277-01 | Qrisp shall provide reflection as a primitive for building quantum algorithms. | ubiquitous | funktional/Leistung | nein | direct |
| QR-0277-02 | reflection shall apply a reflection around the state prepared by state_function. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0277-03 | reflection shall accept qargs of type QuantumVariable \| QuantumArray \| list[QuantumVariable \| QuantumArray]. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0277-04 | While operating in tracing mode, reflection shall compile more efficiently. | state_driven | funktional/Leistung | nein | indirect |
| QR-0277-05 | The diffuser shall apply the reflection primitive. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0277-06 | amplitude_amplification shall accept args of type QuantumVariable \| QuantumArray \| list[QuantumVariable \| QuantumArray]. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0277-07 | QAE shall accept args of type QuantumVariable \| QuantumArray \| list[QuantumVariable \| QuantumArray]. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0277-08 | grovers_alg shall execute Grover's algorithm when qv_list is a QuantumArray. | event_driven | Schnittstelle | nein | indirect |

#### PR 279

[github.com/eclipse-qrisp/Qrisp/pull/279](https://github.com/eclipse-qrisp/Qrisp/pull/279) · 9 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0279-01 | The q_min shall return the minimum of two QuantumFloat values. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0279-02 | The q_max shall return the maximum of two QuantumFloat values. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0279-03 | The q_floor shall compute the floor of a QuantumFloat. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0279-04 | The q_ceil shall compute the ceiling of a QuantumFloat. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0279-05 | The q_fractional shall extract the fractional part of a QuantumFloat. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0279-06 | The q_round shall round a QuantumFloat to the nearest integer. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0279-07 | The q_modf shall split a QuantumFloat into integer and fractional components. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0279-08 | When a ceiling operation would result in overflow, q_ceil shall perform the operation modularly. | event_driven | Schnittstelle | nein | indirect |
| QR-0279-09 | When a rounding operation would result in overflow, q_round shall perform the operation modularly. | event_driven | Schnittstelle | nein | indirect |

#### PR 283

[github.com/eclipse-qrisp/Qrisp/pull/283](https://github.com/eclipse-qrisp/Qrisp/pull/283) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0283-01 | When apply_lcd_hamiltonian is called, apply_lcd_hamiltonian shall evolve the supplied quantum variable under the LCD Hamiltonian for the supplied timestep count. | event_driven | funktional/Leistung | nein | indirect |
| QR-0283-02 | When LCD_routine is called, LCD_routine shall return the final statevector and measurement result dictionary for the supplied quantum variable. | event_driven | funktional/Leistung | nein | indirect |

#### PR 284

[github.com/eclipse-qrisp/Qrisp/pull/284](https://github.com/eclipse-qrisp/Qrisp/pull/284) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0284-01 | The optimization_routine shall minimize the expectation value of the QUBO Hamiltonian. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0284-02 | When COLD_routine obtains optimal control-pulse parameters, the COLD_routine shall apply the COLD Hamiltonian with the optimal control-pulse parameters. | event_driven | funktional/Leistung | nein | indirect |
| QR-0284-03 | When apply_cold_hamiltonian executes a time step, the apply_cold_hamiltonian shall include the control-pulse Hamiltonian contribution. | event_driven | funktional/Leistung | nein | indirect |

#### PR 286

[github.com/eclipse-qrisp/Qrisp/pull/286](https://github.com/eclipse-qrisp/Qrisp/pull/286) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0286-01 | Qrisp shall implement a Decoded Quantum Interferometry algorithm for MAX-XOR-SAT problem instances. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0286-02 | The DQI tutorial shall document Qrisp's implementation of Decoded Quantum Interferometry. | ubiquitous | Prozess | nein | indirect |

#### PR 289

[github.com/eclipse-qrisp/Qrisp/pull/289](https://github.com/eclipse-qrisp/Qrisp/pull/289) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0289-01 | When COLD_routine is invoked, COLD_routine shall determine control-pulse parameters by minimizing the expectation value of the QUBO Hamiltonian. | event_driven | funktional/Leistung | nein | indirect |
| QR-0289-02 | When adding QubitOperator instances with a SymPy symbolic resulting coefficient, QubitOperator shall retain the symbolic coefficient. | event_driven | Schnittstelle | nein | indirect |
| QR-0289-03 | When subtracting QubitOperator instances with a SymPy symbolic resulting coefficient, QubitOperator shall retain the symbolic coefficient. | event_driven | Schnittstelle | nein | indirect |
| QR-0289-04 | When multiplying a QubitOperator by a SymPy Basic scalar, QubitOperator shall represent the scalar as a QubitOperator coefficient. | event_driven | Schnittstelle | nein | indirect |
| QR-0289-05 | When apply_threshold processes a QubitOperator term with a SymPy symbolic coefficient, QubitOperator shall retain the term. | event_driven | Schnittstelle | nein | indirect |

#### PR 290

[github.com/eclipse-qrisp/Qrisp/pull/290](https://github.com/eclipse-qrisp/Qrisp/pull/290) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0290-01 | When QubitOperator multiplication receives an operand outside the types int, float, complex, and QubitOperator, QubitOperator shall raise a TypeError. | event_driven | Schnittstelle | nein | indirect |

#### PR 291

[github.com/eclipse-qrisp/Qrisp/pull/291](https://github.com/eclipse-qrisp/Qrisp/pull/291) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0291-01 | Qrisp shall implement the COLD method for QUBO problems. | ubiquitous | funktional/Leistung | nein | direct |
| QR-0291-02 | When optimization moves away from the last parameter point, CRABObjective shall refresh the random pulse distribution. | event_driven | funktional/Leistung | nein | indirect |

#### PR 292

[github.com/eclipse-qrisp/Qrisp/pull/292](https://github.com/eclipse-qrisp/Qrisp/pull/292) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0292-01 | When reversed is true, QubitOperator.from_matrix shall reverse the endianness of the resulting operator. | event_driven | Schnittstelle | nein | indirect |
| QR-0292-02 | QubitOperator.pauli_block_encoding shall return a block encoding of the operator based on its Pauli decomposition. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0292-03 | QubitOperator.pauli_block_encoding shall return a tuple containing U_func, G_func, and n. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0292-04 | QubitOperator.pauli_block_encoding shall return U_func that applies the block encoding unitary to operand and case QuantumVariables. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0292-05 | QubitOperator.pauli_block_encoding shall return G_func that prepares the block encoding state in an auxiliary case QuantumVariable. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0292-06 | QubitOperator.pauli_block_encoding shall return n as the number of qubits in the auxiliary case QuantumVariable. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 293

[github.com/eclipse-qrisp/Qrisp/pull/293](https://github.com/eclipse-qrisp/Qrisp/pull/293) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0293-01 | When a substitution dictionary is supplied, the Qrisp-to-PennyLane conversion function shall substitute abstract gate parameters with the dictionary's values. | event_driven | funktional/Leistung | nein | indirect |
| QR-0293-02 | When a Qrisp circuit contains a measurement operation, the Qrisp-to-PennyLane conversion function shall emit a PennyLane mid-circuit measurement on the target wires. | event_driven | funktional/Leistung | nein | indirect |
| QR-0293-03 | When a Qrisp circuit contains a controlled operation, the Qrisp-to-PennyLane conversion function shall use the operation's control wires and control-state values in the PennyLane controlled operation. | event_driven | funktional/Leistung | nein | indirect |
| QR-0293-04 | When a Qrisp circuit contains an adjoint gate, the Qrisp-to-PennyLane conversion function shall emit a PennyLane adjoint of the base operation. | event_driven | funktional/Leistung | nein | indirect |
| QR-0293-05 | Where PennyLane is unavailable, when qml_converter is invoked, qml_converter shall raise an ImportError. | complex | Schnittstelle | nein | indirect |

#### PR 294

[github.com/eclipse-qrisp/Qrisp/pull/294](https://github.com/eclipse-qrisp/Qrisp/pull/294) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0294-01 | When invoked with a Hermitian matrix A and vector b, CKS shall prepare an approximation of the normalized solution A⁻¹b. | event_driven | funktional/Leistung | nein | indirect |
| QR-0294-02 | When invoked with a block-encoding tuple and a callable b state preparation, CKS shall prepare an approximation of the normalized linear-system solution. | event_driven | funktional/Leistung | nein | indirect |
| QR-0294-03 | If A is a block-encoding tuple and kappa is omitted, then CKS_parameters shall raise an exception. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0294-04 | QubitOperator.pauli_block_encoding shall return a block-encoding unitary, a block-encoding state-preparation function, and an auxiliary-qubit count. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0294-05 | When reverse_endianness is True, QubitOperator.from_matrix shall represent the matrix with reversed endianness. | event_driven | Schnittstelle | nein | indirect |

#### PR 295

[github.com/eclipse-qrisp/Qrisp/pull/295](https://github.com/eclipse-qrisp/Qrisp/pull/295) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0295-01 | LCD_routine shall produce measurement results for the supplied QUBO matrix. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0295-02 | COLD_routine shall produce measurement results for the supplied QUBO matrix. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0295-03 | evaluate shall write an evaluation CSV file. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 296

[github.com/eclipse-qrisp/Qrisp/pull/296](https://github.com/eclipse-qrisp/Qrisp/pull/296) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0296-01 | When a caller invokes Jaspr.to_mlir, Jaspr shall return an xDSL module representing the quantum computation. | event_driven | Schnittstelle | nein | indirect |
| QR-0296-02 | When a caller invokes Jaspr.to_catalyst_mlir, Jaspr shall provide Catalyst-based MLIR. | event_driven | Schnittstelle | nein | indirect |
| QR-0296-03 | When Jaspr.to_mlir generates MLIR, Jaspr shall represent quantum operations using Jasp dialect operations. | event_driven | funktional/Leistung | nein | indirect |
| QR-0296-04 | When StableHLO control flow operations involve quantum types, the MLIR generation process shall rewrite them to SCF dialect operations. | event_driven | funktional/Leistung | nein | indirect |
| QR-0296-05 | The MLIR Interface documentation shall specify the Jasp dialect's operations and types. | ubiquitous | Prozess | nein | indirect |

#### PR 297

[github.com/eclipse-qrisp/Qrisp/pull/297](https://github.com/eclipse-qrisp/Qrisp/pull/297) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0297-01 | DCQOProblem shall compute λ(t, T) and its time derivative for each timestep. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0297-02 | DCQOProblem shall simulate the local counterdiabatic driving Hamiltonian on a quantum argument. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0297-03 | DCQOProblem shall simulate the counterdiabatic optimized local driving Hamiltonian on a quantum argument. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0297-04 | Where H_control is not given, DCQOProblem shall use the LCD method. | optional_feature | Schnittstelle | nein | indirect |
| QR-0297-05 | When qarg_prep is not provided, DCQOProblem shall prepare the quantum argument in the uniform superposition state. | event_driven | Schnittstelle | nein | indirect |
| QR-0297-06 | When callback is True, DCQOProblem shall store intermediate results. | event_driven | Schnittstelle | nein | indirect |

#### PR 299

[github.com/eclipse-qrisp/Qrisp/pull/299](https://github.com/eclipse-qrisp/Qrisp/pull/299) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0299-01 | The qdrift function shall approximate the time evolution of a quantum state under a Hamiltonian using the QDRIFT algorithm. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0299-02 | The qdrift function shall apply N sampled exponentials to the quantum state. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0299-03 | The qdrift function shall select a Hamiltonian term for a QDRIFT sample with probability equal to the absolute value of its coefficient divided by the sum of coefficient absolute values. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0299-04 | The qdrift function shall set the QDRIFT time-step to the total absolute Hamiltonian-coefficient weight multiplied by the total simulation time and divided by N. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0299-05 | Where use_arctan is True, the qdrift function shall use the arctangent of the QDRIFT time-step for sampled exponentials. | optional_feature | funktional/Leistung | nein | indirect |
| QR-0299-06 | The qdrift function shall apply a sampled Pauli term with a time-step whose sign matches the associated Hamiltonian coefficient. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 303

[github.com/eclipse-qrisp/Qrisp/pull/303](https://github.com/eclipse-qrisp/Qrisp/pull/303) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0303-01 | When supplied with a QUBO matrix and outcome probabilities, qubo_cost shall return the probability-weighted quadratic cost. | event_driven | Schnittstelle | nein | indirect |
| QR-0303-02 | When a DCQOProblem lacks a cached time grid, DCQOProblem shall compute and cache lambda and lambda-dot values before applying the LCD Hamiltonian. | event_driven | funktional/Leistung | nein | indirect |
| QR-0303-03 | When QubitOperator.__iadd__ adds a term whose resulting coefficient is a SymPy Basic instance, QubitOperator.__iadd__ shall retain the term. | event_driven | funktional/Leistung | nein | insufficient |

#### PR 304

[github.com/eclipse-qrisp/Qrisp/pull/304](https://github.com/eclipse-qrisp/Qrisp/pull/304) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0304-01 | When cgphase_gate is configured with ctrl_state=0, cgphase_gate shall use its second-to-last qubit for the control-state inversion. | event_driven | funktional/Leistung | nein | indirect |

#### PR 305

[github.com/eclipse-qrisp/Qrisp/pull/305](https://github.com/eclipse-qrisp/Qrisp/pull/305) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0305-01 | QuantumCircuit shall provide an mcz method that instructs a multi-controlled Z gate on a supplied qubit list. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0305-02 | QuantumCircuit shall provide an mcp method that instructs a multi-controlled P gate on a supplied qubit list. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0305-03 | QuantumCircuit shall provide a crz method that instructs a controlled RZ gate on two qubits. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0305-04 | If phi is not a float or sympy.Symbol, then QuantumCircuit.mcp shall raise ValueError. | unwanted_behaviour | Schnittstelle | **ja** | indirect |
| QR-0305-05 | If phi is not a float or sympy.Symbol, then QuantumCircuit.crz shall raise ValueError. | unwanted_behaviour | Schnittstelle | **ja** | indirect |

#### PR 306

[github.com/eclipse-qrisp/Qrisp/pull/306](https://github.com/eclipse-qrisp/Qrisp/pull/306) · 10 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0306-01 | QuantumVariable.init_state shall initialize a quantum variable from an explicit complex statevector of length 2^n. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0306-02 | When initialized with an array-like input, QuantumVariable.init_state shall interpret amplitudes in the order returned by the statevector method. | event_driven | Schnittstelle | nein | indirect |
| QR-0306-03 | QuantumVariable.init_state shall accept the method choices "auto", "qiskit", and "qswitch". | ubiquitous | Schnittstelle | nein | indirect |
| QR-0306-04 | When method is "auto" outside Jasp mode, QuantumVariable.init_state shall use the Qiskit-based initializer. | event_driven | funktional/Leistung | nein | indirect |
| QR-0306-05 | When method is "auto" during Jasp mode, QuantumVariable.init_state shall use the internal qswitch initializer. | event_driven | funktional/Leistung | nein | indirect |
| QR-0306-06 | If method="qiskit" is used in Jasp mode, then QuantumVariable.init_state shall raise ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0306-07 | While executing outside Jasp mode, if a supplied statevector length differs from 2^qv.size, then prepare shall raise ValueError. | complex | Schnittstelle | nein | indirect |
| QR-0306-08 | While executing outside Jasp mode, if a supplied statevector has zero norm, then prepare shall raise ValueError. | complex | Schnittstelle | nein | indirect |
| QR-0306-09 | While executing outside Jasp mode, if qv is not fresh, then prepare shall raise ValueError. | complex | Schnittstelle | nein | indirect |
| QR-0306-10 | When a nonzero statevector is supplied outside Jasp mode, prepare shall normalize the statevector before initialization. | event_driven | funktional/Leistung | nein | indirect |

#### PR 307

[github.com/eclipse-qrisp/Qrisp/pull/307](https://github.com/eclipse-qrisp/Qrisp/pull/307) · 7 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0307-01 | QuantumCircuit shall provide a to_cirq method that returns a Cirq QuantumCircuit representing the QuantumCircuit. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0307-02 | When cirq_qubits is supplied, convert_to_cirq shall map each Qrisp circuit qubit to the Cirq qubit at the corresponding index. | event_driven | Schnittstelle | nein | indirect |
| QR-0307-03 | When a composite gate has a definition and lacks a direct Cirq equivalent, convert_to_cirq shall recursively convert the gate definition. | event_driven | funktional/Leistung | nein | direct |
| QR-0307-04 | When a Qrisp circuit contains a global phase gate, convert_to_cirq shall skip the global phase gate during conversion. | event_driven | funktional/Leistung | nein | indirect |
| QR-0307-05 | If a Qrisp gate cannot be converted or transpiled, then convert_to_cirq shall raise a ValueError identifying the unsupported gate. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0307-06 | Qrisp shall treat Cirq as an optional dependency. | ubiquitous | Qualität (nicht funktional) | nein | insufficient |
| QR-0307-07 | QuantumCircuit documentation shall list QuantumCircuit.to_cirq under Interfacing. | ubiquitous | Prozess | nein | indirect |

#### PR 310

[github.com/eclipse-qrisp/Qrisp/pull/310](https://github.com/eclipse-qrisp/Qrisp/pull/310) · 9 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0310-01 | While executing in JASP mode, dicke_state shall prepare an equal superposition of Dicke states for the specified Hamming weight. | state_driven | funktional/Leistung | nein | indirect |
| QR-0310-02 | dicke_state shall accept QuantumArray inputs. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0310-03 | When invoked with a QuantumVariable in the zero state, dicke_divide_and_conquer shall prepare an equal superposition of states with the specified Hamming weight. | event_driven | funktional/Leistung | nein | indirect |
| QR-0310-04 | CKS shall apply the non-unitary operator A⁻¹ to the input state \|b⟩. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0310-05 | QubitOperator.pauli_block_encoding shall return a block encoding of the operator. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0310-06 | Where reverse_endianness is True, QubitOperator.from_matrix shall represent matrix factors using reversed endianness. | optional_feature | Schnittstelle | nein | indirect |
| QR-0310-07 | If append_operation receives an empty qubit list, then append_operation shall return without requiring a QuantumSession. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0310-08 | When batch execution raises an exception on the main thread, batched_backend.dispatch shall raise the exception. | event_driven | funktional/Leistung | nein | indirect |
| QR-0310-09 | run_batch_iqm shall retain each IQM count key after removing non-word characters. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 313

[github.com/eclipse-qrisp/Qrisp/pull/313](https://github.com/eclipse-qrisp/Qrisp/pull/313) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0313-01 | Where the COLD method is selected, DCQOProblem shall compute g(lambda) and its derivative for the time grid. | optional_feature | funktional/Leistung | nein | indirect |
| QR-0313-02 | When lamdot is a float, DCQOProblem.__precompute_timegrid shall store an N_steps-length sequence of lamdot values. | event_driven | funktional/Leistung | nein | indirect |
| QR-0313-03 | When alpha_vec is true, the alpha function in create_COLD_instance shall provide an N-element alpha vector. | event_driven | Schnittstelle | nein | indirect |
| QR-0313-04 | The alpha function in create_LCD_instance shall provide an N-element alpha vector. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 314

[github.com/eclipse-qrisp/Qrisp/pull/314](https://github.com/eclipse-qrisp/Qrisp/pull/314) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0314-01 | While tracing mode is inactive, Jasp prefix control shall repeatedly apply body_fun to the loop value while cond_fun returns true. | state_driven | funktional/Leistung | nein | indirect |
| QR-0314-02 | While tracing mode is inactive, Jasp prefix control shall return the result of the branch selected by pred. | state_driven | funktional/Leistung | nein | indirect |

#### PR 315

[github.com/eclipse-qrisp/Qrisp/pull/315](https://github.com/eclipse-qrisp/Qrisp/pull/315) · 9 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0315-01 | lanczos_expvals shall obtain Chebyshev expectation values. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0315-02 | build_S_H_from_Tk shall construct overlap and Hamiltonian subspace matrices from Chebyshev expectation values. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0315-03 | regularize_S_H shall project the overlap and Hamiltonian matrices onto the subspace with well-conditioned eigenvalues. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0315-04 | lanczos_alg shall return the lowest generalized eigenvalue as a ground-state energy estimate. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0315-05 | When executed in Jasp, the Lanczos implementation shall solve the generalized eigenvalue problem. | event_driven | Schnittstelle | nein | indirect |
| QR-0315-06 | When state_function is omitted, reflection shall perform a reflection around the \|0> state. | event_driven | Schnittstelle | nein | indirect |
| QR-0315-07 | GQET shall return a BlockEncoding representing a polynomial transformation of the supplied operator. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0315-08 | convolve shall perform cyclic convolution of a quantum state with a filter. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0315-09 | When given a signal and frequency cutoff k, fourier_series_loader shall preserve frequencies in the range [-k,k]. | event_driven | funktional/Leistung | nein | indirect |

#### PR 316

[github.com/eclipse-qrisp/Qrisp/pull/316](https://github.com/eclipse-qrisp/Qrisp/pull/316) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0316-01 | When supplied a BlockEncoding and a sequence of phase angles, QSVT shall return a BlockEncoding of the transformed operator P(A/alpha). | event_driven | Schnittstelle | nein | indirect |
| QR-0316-02 | When supplied a BlockEncoding, target precision eps, and condition number kappa, QSVT_inversion shall return a BlockEncoding of the transformed operator A^-1. | event_driven | Schnittstelle | nein | indirect |

#### PR 317

[github.com/eclipse-qrisp/Qrisp/pull/317](https://github.com/eclipse-qrisp/Qrisp/pull/317) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0317-01 | When a loop equation is reinterpreted, the Jaxpr language shall classify the first cond_nconsts loop variables as condition constants. | event_driven | funktional/Leistung | nein | indirect |
| QR-0317-02 | When a loop equation is reinterpreted, the Jaxpr language shall classify the body_nconsts loop variables following the condition constants as body constants. | event_driven | funktional/Leistung | nein | indirect |
| QR-0317-03 | When a loop equation is reinterpreted, the Jaxpr language shall classify loop variables following the body constants as carries. | event_driven | funktional/Leistung | nein | indirect |

#### PR 318

[github.com/eclipse-qrisp/Qrisp/pull/318](https://github.com/eclipse-qrisp/Qrisp/pull/318) · 15 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0318-01 | BlockEncoding shall construct a BlockEncoding from a 2-D array. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0318-02 | BlockEncoding shall construct a BlockEncoding using the Linear Combination of Unitaries protocol. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0318-03 | BlockEncoding shall construct a BlockEncoding from an operator. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0318-04 | BlockEncoding shall apply its unitary to given operands. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0318-05 | BlockEncoding shall apply a BlockEncoding using repeat-until-success. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0318-06 | BlockEncoding shall estimate the quantum resources required for a BlockEncoding. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0318-07 | BlockEncoding shall return a BlockEncoding of the sum of two operators. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0318-08 | BlockEncoding shall return a BlockEncoding of the product of two operators. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0318-09 | BlockEncoding shall return a BlockEncoding of a scaled operator. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0318-10 | BlockEncoding shall return a BlockEncoding of a negated operator. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0318-11 | BlockEncoding shall return a BlockEncoding of the difference between two operators. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0318-12 | BlockEncoding shall return a BlockEncoding of the Kronecker product of two operators. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0318-13 | BlockEncoding shall return a BlockEncoding approximating matrix inversion of the operator. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0318-14 | BlockEncoding shall return a BlockEncoding representing a polynomial transformation of the operator. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0318-15 | BlockEncoding shall return a BlockEncoding approximating Hamiltonian simulation of the operator. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 319

[github.com/eclipse-qrisp/Qrisp/pull/319](https://github.com/eclipse-qrisp/Qrisp/pull/319) · 11 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0319-01 | QubitOperator shall expose a qdrift method. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0319-02 | q_max shall return the maximum value of two QuantumFloat inputs. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0319-03 | q_min shall return the minimum value of two QuantumFloat inputs. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0319-04 | q_floor shall return an out-of-place QuantumFloat containing the floor of its input. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0319-05 | q_ceil shall return an out-of-place QuantumFloat containing the ceiling of its input. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0319-06 | If a q_ceil operation would overflow, then q_ceil shall perform the operation modularly. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0319-07 | q_round shall return an out-of-place QuantumFloat rounded to the first significant digit. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0319-08 | q_fractional shall return an out-of-place QuantumFloat containing the fractional part of its input. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0319-09 | BigInteger shall support integer representations with bit widths beyond 64 bits. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0319-10 | q_montgomery_reduction shall perform in-place Montgomery reduction on a concatenated QuantumFloat. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0319-11 | cq_montgomery_multiply shall return the product X*y modulo N in standard representation. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 321

[github.com/eclipse-qrisp/Qrisp/pull/321](https://github.com/eclipse-qrisp/Qrisp/pull/321) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0321-01 | While iterating i in range(1, qv.size), the ghz function shall apply a controlled-X gate from qv[0] to qv[i]. | state_driven | funktional/Leistung | nein | insufficient |
| QR-0321-02 | When a transpile_predicate returns True for QFT_dg, QuantumCircuit shall transpile QFT_dg. | event_driven | Schnittstelle | nein | indirect |

#### PR 322

[github.com/eclipse-qrisp/Qrisp/pull/322](https://github.com/eclipse-qrisp/Qrisp/pull/322) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0322-01 | QubitOperator.qdrift shall provide a callable that simulates quantum-state time evolution under the operator using QDrift. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0322-02 | While forward_evolution is False, QubitOperator.qdrift shall execute reverse time evolution e^{itH}. | state_driven | funktional/Leistung | nein | indirect |
| QR-0322-03 | QubitOperator.qdrift shall provide a callable with invocation signature (qarg, t=1, samples=100, iter=1). | ubiquitous | Schnittstelle | nein | indirect |

#### PR 325

[github.com/eclipse-qrisp/Qrisp/pull/325](https://github.com/eclipse-qrisp/Qrisp/pull/325) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0325-01 | When a slice of a DynamicQubitArray has a step other than 1, DynamicQubitArray shall raise NotImplementedError. | event_driven | funktional/Leistung | nein | indirect |

#### PR 326

[github.com/eclipse-qrisp/Qrisp/pull/326](https://github.com/eclipse-qrisp/Qrisp/pull/326) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0326-01 | If direct solution raises a linear-algebra error, then solve_params shall return a least-squares solution. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0326-02 | Where uniform is true, solve_alpha_gamma_chi shall produce length-N AGP coefficient arrays whose entries are identical. | optional_feature | funktional/Leistung | nein | indirect |
| QR-0326-03 | When applying an LCD Hamiltonian timestep, DCQOProblem shall include the AGP contribution calculated from the AGP coefficients at that timestep's lambda value. | event_driven | funktional/Leistung | nein | indirect |

#### PR 327

[github.com/eclipse-qrisp/Qrisp/pull/327](https://github.com/eclipse-qrisp/Qrisp/pull/327) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0327-01 | QubitOperator.qdrift shall apply a QDRIFT approximation of Hamiltonian time evolution to the supplied QuantumVariable. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0327-02 | QubitOperator.qdrift shall sample Hamiltonian terms independently with probability equal to each coefficient magnitude divided by the sum of coefficient magnitudes. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0327-03 | When use_arctan is True, QubitOperator.qdrift shall use the arctangent of the Hamiltonian coefficient absolute-sum multiplied by t and divided by N as its timestep. | event_driven | Schnittstelle | nein | indirect |

#### PR 331

[github.com/eclipse-qrisp/Qrisp/pull/331](https://github.com/eclipse-qrisp/Qrisp/pull/331) · 7 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0331-01 | Qrisp shall deprecate BackendClient, BackendServer, and VirtualBackend with QrispDeprecationWarning. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0331-02 | Qrisp shall provide a Backend class. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0331-03 | When a concrete Backend implementation exposes calibration-dependent values, the concrete Backend implementation shall include a calibration anchor alongside the values. | event_driven | Schnittstelle | nein | indirect |
| QR-0331-04 | Backend shall report the total physical-qubit count it exposes through num_qubits. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0331-05 | Backend connectivity shall represent currently executable two-qubit gates. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0331-06 | When a Backend subclass exposes backend-specific capabilities, the Backend subclass shall expose them as concrete typed properties. | event_driven | Schnittstelle | nein | indirect |
| QR-0331-07 | Qrisp shall exclude the network-dependency set flask, waitress, pyyaml, requests from its installation dependencies. | ubiquitous | Qualität (nicht funktional) | nein | direct |

#### PR 333

[github.com/eclipse-qrisp/Qrisp/pull/333](https://github.com/eclipse-qrisp/Qrisp/pull/333) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0333-01 | The README shall link the encryption-breaking tutorial reference to the Shor tutorial. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0333-02 | The README shall link the More examples reference to the tutorial index. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 338

[github.com/eclipse-qrisp/Qrisp/pull/338](https://github.com/eclipse-qrisp/Qrisp/pull/338) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0338-01 | While tracing mode is active, when a comparison operation is invoked on a QuantumModulus value, QuantumModulus shall evaluate the comparison operation. | complex | funktional/Leistung | nein | indirect |

#### PR 339

[github.com/eclipse-qrisp/Qrisp/pull/339](https://github.com/eclipse-qrisp/Qrisp/pull/339) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0339-01 | When invoked with a U3 matrix and a Qubit, the unitary function shall apply the U3 matrix to the Qubit. | event_driven | Schnittstelle | nein | indirect |

#### PR 341

[github.com/eclipse-qrisp/Qrisp/pull/341](https://github.com/eclipse-qrisp/Qrisp/pull/341) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0341-01 | When a caller supplies a device to qjit, qjit shall execute the function on that device. | event_driven | Schnittstelle | nein | indirect |
| QR-0341-02 | If no device is provided, then jaspr_to_catalyst_function shall use the lightning.qubit device. | unwanted_behaviour | funktional/Leistung | nein | indirect |

#### PR 342

[github.com/eclipse-qrisp/Qrisp/pull/342](https://github.com/eclipse-qrisp/Qrisp/pull/342) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0342-01 | Qrisp shall declare jax version 0.6.2 as an installation dependency. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0342-02 | Qrisp shall declare jaxlib version 0.6.2 as an installation dependency. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 343

[github.com/eclipse-qrisp/Qrisp/pull/343](https://github.com/eclipse-qrisp/Qrisp/pull/343) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0343-01 | The Qrisp documentation shall demonstrate calculating an expectation value with QubitOperator.expectation_value. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 344

[github.com/eclipse-qrisp/Qrisp/pull/344](https://github.com/eclipse-qrisp/Qrisp/pull/344) · 9 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0344-01 | When addition is invoked on a QuantumArray, QuantumArray shall return a new QuantumArray containing the element-wise sum. | event_driven | Schnittstelle | nein | indirect |
| QR-0344-02 | When subtraction is invoked on a QuantumArray, QuantumArray shall return a new QuantumArray containing the element-wise difference. | event_driven | Schnittstelle | nein | indirect |
| QR-0344-03 | When multiplication is invoked on a QuantumArray, QuantumArray shall return a new QuantumArray containing the element-wise product. | event_driven | Schnittstelle | nein | indirect |
| QR-0344-04 | When a comparison operator is invoked on QuantumArray operands, QuantumArray shall produce a QuantumArray containing the element-wise comparison result. | event_driven | Schnittstelle | nein | indirect |
| QR-0344-05 | If a QuantumArray operand of an element-wise operation has a qtype other than QuantumFloat, then QuantumArray shall raise TypeError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0344-06 | If QuantumArray operands of an element-wise operation have different shapes, then QuantumArray shall raise ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0344-07 | If a NumPy array operand of an element-wise operation has a different shape from a QuantumArray, then QuantumArray shall raise ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0344-08 | When a QuantumArray is the target of a redirected quantum function, QuantumArray shall receive the function result in corresponding target elements. | event_driven | Schnittstelle | nein | indirect |
| QR-0344-09 | When in-place addition is invoked on a QuantumArray with a scalar, QuantumArray shall update its elements with the element-wise sums. | event_driven | Schnittstelle | nein | indirect |

#### PR 345

[github.com/eclipse-qrisp/Qrisp/pull/345](https://github.com/eclipse-qrisp/Qrisp/pull/345) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0345-01 | While executing in boolean_simulation mode, singular_shift shall cyclically shift the input qubit register by one position, placing its final-position bit at position zero. | state_driven | funktional/Leistung | nein | indirect |
| QR-0345-02 | While executing in boolean_simulation mode with shift_amount set to 1, cyclic_shift shall cyclically shift the input qubit register by one position, placing its final-position bit at position zero. | state_driven | funktional/Leistung | nein | indirect |

#### PR 346

[github.com/eclipse-qrisp/Qrisp/pull/346](https://github.com/eclipse-qrisp/Qrisp/pull/346) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0346-01 | The workflow shall check direct GitHub Actions dependencies for version updates weekly. | ubiquitous | Prozess | nein | indirect |
| QR-0346-02 | The workflow shall limit open dependency-update pull requests for direct GitHub Actions dependencies to 10. | ubiquitous | Prozess | nein | indirect |
| QR-0346-03 | The workflow shall exclude SemVer patch updates from direct GitHub Actions dependency updates. | ubiquitous | Prozess | nein | indirect |
| QR-0346-04 | The workflow shall check direct pip dependencies for version updates weekly. | ubiquitous | Prozess | nein | indirect |
| QR-0346-05 | The workflow shall limit open dependency-update pull requests for direct pip dependencies to 10. | ubiquitous | Prozess | nein | indirect |
| QR-0346-06 | The workflow shall exclude SemVer patch updates from direct pip dependency updates. | ubiquitous | Prozess | nein | indirect |

#### PR 350

[github.com/eclipse-qrisp/Qrisp/pull/350](https://github.com/eclipse-qrisp/Qrisp/pull/350) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0350-01 | When cdkpm_adder receives an operand of ALLOWED_CDKPM_ADDER_QUANTUM_TYPES paired with a classical operand, cdkpm_adder shall accept the operands. | event_driven | Schnittstelle | nein | indirect |
| QR-0350-02 | When cdkpm_adder receives two operands of ALLOWED_CDKPM_ADDER_QUANTUM_TYPES, cdkpm_adder shall accept the operands. | event_driven | Schnittstelle | nein | indirect |
| QR-0350-03 | When cdkpm_adder receives operands with unequal sizes, cdkpm_adder shall extend the smaller operand to the larger operand's size. | event_driven | funktional/Leistung | nein | indirect |

#### PR 352

[github.com/eclipse-qrisp/Qrisp/pull/352](https://github.com/eclipse-qrisp/Qrisp/pull/352) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0352-01 | The qswitch shall expose the interface qswitch(case, branches, *operands, method="auto", branch_amount=None). | ubiquitous | Schnittstelle | nein | indirect |
| QR-0352-02 | When called through the deprecated qswitch(operand, case, case_function, method="auto", case_amount=None) interface, the qswitch shall execute the call. | event_driven | Schnittstelle | nein | indirect |
| QR-0352-03 | When called through the deprecated qswitch interface, the qswitch shall issue a FutureWarning. | event_driven | Schnittstelle | nein | indirect |
| QR-0352-04 | When parallel compilation is requested with more than one operand, the qswitch shall raise NotImplementedError. | event_driven | funktional/Leistung | nein | indirect |

#### PR 354

[github.com/eclipse-qrisp/Qrisp/pull/354](https://github.com/eclipse-qrisp/Qrisp/pull/354) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0354-01 | Qrisp shall operate with Python versions 3.10 through 3.12. | ubiquitous | Qualität (nicht funktional) | nein | indirect |

#### PR 358

[github.com/eclipse-qrisp/Qrisp/pull/358](https://github.com/eclipse-qrisp/Qrisp/pull/358) · 7 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0358-01 | While execution is not in tracing mode, prepare shall reject a target array whose length differs from 2 raised to the size of qv. | state_driven | Schnittstelle | nein | indirect |
| QR-0358-02 | While execution is not in tracing mode, prepare shall reject a target array with zero norm. | state_driven | Schnittstelle | nein | indirect |
| QR-0358-03 | While execution is not in tracing mode, prepare shall normalize the target amplitude vector before state preparation. | state_driven | funktional/Leistung | nein | indirect |
| QR-0358-04 | prepare_qswitch shall use little-endian computational-basis ordering by default. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0358-05 | When big_endianness is True, prepare_qswitch shall use big-endian computational-basis ordering. | event_driven | Schnittstelle | nein | indirect |
| QR-0358-06 | QuantumVariable.init_state shall use little-endian indexing for explicit statevector input. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0358-07 | QuantumCircuit.statevector_array shall return statevector amplitudes in big-endian index order. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 359

[github.com/eclipse-qrisp/Qrisp/pull/359](https://github.com/eclipse-qrisp/Qrisp/pull/359) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0359-01 | When used for a 2048-bit Shor algorithm, count_ops shall produce operation resource counts. | event_driven | funktional/Leistung | nein | indirect |
| QR-0359-02 | Qrisp shall insert the non-constant outputs of a while-loop into the interpretation context. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0359-03 | Qrisp shall obtain a while-loop condition's constants from the condition-constant portion of the loop input values. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 360

[github.com/eclipse-qrisp/Qrisp/pull/360](https://github.com/eclipse-qrisp/Qrisp/pull/360) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0360-01 | When a Jasp-compatible function is decorated, depth shall return the quantum computation's circuit depth as an integer. | event_driven | Schnittstelle | nein | indirect |
| QR-0360-02 | When a gate has a definition, depth shall calculate the macro-gate depth according to the operations in the gate definition. | event_driven | funktional/Leistung | nein | indirect |
| QR-0360-03 | When an additional metric is added, the profiling interpreter shall permit its addition without modification. | event_driven | Qualität (nicht funktional) | nein | indirect |
| QR-0360-04 | Where a max_qubits value is supplied, depth shall use the value as the maximum number of qubits supported for depth computation. | optional_feature | Schnittstelle | nein | indirect |
| QR-0360-05 | When count_ops processes a measurement on one qubit, count_ops shall increment the measurement count once. | event_driven | funktional/Leistung | nein | indirect |

#### PR 361

[github.com/eclipse-qrisp/Qrisp/pull/361](https://github.com/eclipse-qrisp/Qrisp/pull/361) · 18 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0361-01 | QuantumCircuit.to_stim shall convert QuantumCircuit objects into stim.Circuit objects. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0361-02 | When requested, QuantumCircuit.to_stim shall return maps correlating Qrisp measurement objects or clbits with Stim measurement-record indices. | event_driven | Schnittstelle | nein | indirect |
| QR-0361-03 | Qrisp shall convert classically controlled Pauli gates to Stim circuits. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0361-04 | extract_stim shall extract the corresponding Stim circuit from a Jasp quantum function. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0361-05 | extract_stim shall separate Qrisp return values from the generated Stim circuit. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0361-06 | Where the compilation target is Stim, StimNoiseGate shall translate to its corresponding noise instruction. | optional_feature | funktional/Leistung | nein | indirect |
| QR-0361-07 | Where the compilation target is not Stim, StimNoiseGate shall act as an identity gate. | optional_feature | funktional/Leistung | nein | indirect |
| QR-0361-08 | parity shall compute the XOR of multiple measurement results. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0361-09 | When parity receives parity results as inputs, parity shall cancel duplicate clbits using symmetric difference. | event_driven | funktional/Leistung | nein | indirect |
| QR-0361-10 | When a parity result is converted to Stim as a detector, parity shall create a DETECTOR instruction. | event_driven | Schnittstelle | nein | indirect |
| QR-0361-11 | When a parity result is converted to Stim as an observable, parity shall create an OBSERVABLE_INCLUDE instruction. | event_driven | Schnittstelle | nein | indirect |
| QR-0361-12 | find_detectors shall identify DETECTOR instructions in quantum error-correction circuits. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0361-13 | When processing a multi-round code, find_detectors shall detect intra-round detectors. | event_driven | funktional/Leistung | nein | indirect |
| QR-0361-14 | When processing a multi-round code, find_detectors shall detect temporal cross-round detectors. | event_driven | funktional/Leistung | nein | indirect |
| QR-0361-15 | When a decorated function receives a non-QuantumArray argument, find_detectors shall treat the argument as a compile-time constant. | event_driven | funktional/Leistung | nein | indirect |
| QR-0361-16 | When return_circuits is True, find_detectors shall append the raw Stim circuit, tqecd-prepared circuit, and annotated circuit to its return value. | event_driven | Schnittstelle | nein | indirect |
| QR-0361-17 | When a discovered detector references a measurement absent from decorated-function return values, find_detectors shall discard the detector. | event_driven | funktional/Leistung | nein | indirect |
| QR-0361-18 | StimBackend shall simulate Qrisp QuantumCircuits using the Stim simulator. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 362

[github.com/eclipse-qrisp/Qrisp/pull/362](https://github.com/eclipse-qrisp/Qrisp/pull/362) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0362-01 | make_jaspr shall omit the garbage_collection keyword argument. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0362-02 | When a RUS trial function returns a termination bool other than True, the RUS decorator shall reset QuantumVariables returned by the trial function. | event_driven | funktional/Leistung | nein | indirect |
| QR-0362-03 | When a RUS trial function returns a termination bool other than True, the RUS decorator shall deallocate QuantumVariables returned by the trial function. | event_driven | funktional/Leistung | nein | indirect |
| QR-0362-04 | During repeated RUS trial iterations, the RUS decorator shall retain non-deallocated local QuantumVariables that the trial function does not return. | state_driven | funktional/Leistung | nein | indirect |

#### PR 363

[github.com/eclipse-qrisp/Qrisp/pull/363](https://github.com/eclipse-qrisp/Qrisp/pull/363) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0363-01 | When a Jax tracing context threshold is passed, QuantumFloat shall retain its signed attribute as static. | event_driven | Schnittstelle | nein | indirect |

#### PR 364

[github.com/eclipse-qrisp/Qrisp/pull/364](https://github.com/eclipse-qrisp/Qrisp/pull/364) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0364-01 | When a jasp.create_qubits operation produces a QubitArray that is neither returned nor used by an operation requiring physical qubits, Jaspr shall remove the operation. | event_driven | funktional/Leistung | nein | indirect |
| QR-0364-02 | If the termination bool returned by a trial function is not True, then the RUS decorator shall reset QuantumVariables returned by the trial function. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0364-03 | If the termination bool returned by a trial function is not True, then the RUS decorator shall deallocate QuantumVariables returned by the trial function. | unwanted_behaviour | funktional/Leistung | nein | indirect |

#### PR 366

[github.com/eclipse-qrisp/Qrisp/pull/366](https://github.com/eclipse-qrisp/Qrisp/pull/366) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0366-01 | q_switch shall execute the branch selected by index with the supplied operands and return that branch's value. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0366-02 | If q_switch detects an implicit variable import, then q_switch shall raise an exception that instructs callers to include the used variables in the body signature. | unwanted_behaviour | funktional/Leistung | nein | indirect |

#### PR 367

[github.com/eclipse-qrisp/Qrisp/pull/367](https://github.com/eclipse-qrisp/Qrisp/pull/367) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0367-01 | When performing a tensor contraction, tensordot shall calculate the resulting array-size estimate as the product of the operand sizes divided by the square of the contraction size. | event_driven | funktional/Leistung | nein | indirect |

#### PR 368

[github.com/eclipse-qrisp/Qrisp/pull/368](https://github.com/eclipse-qrisp/Qrisp/pull/368) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0368-01 | QubitOperator.qdrift shall return a callable that implements QDrift Hamiltonian simulation. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0368-02 | When forward_evolution is False, QubitOperator.qdrift shall execute the inverse Hamiltonian time-evolution operator e^(itH). | event_driven | Schnittstelle | nein | indirect |
| QR-0368-03 | QubitOperator.qdrift shall be traceable by JAX. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 370

[github.com/eclipse-qrisp/Qrisp/pull/370](https://github.com/eclipse-qrisp/Qrisp/pull/370) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0370-01 | If Cirq is unavailable, then convert_to_cirq shall raise an ImportError explaining that Cirq must be installed to use the Qrisp-to-Cirq converter. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0370-02 | When a Qrisp circuit contains a gphase operation, convert_to_cirq shall add a Cirq global phase whose angle equals the gphase parameter. | event_driven | funktional/Leistung | nein | indirect |

#### PR 371

[github.com/eclipse-qrisp/Qrisp/pull/371](https://github.com/eclipse-qrisp/Qrisp/pull/371) · 7 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0371-01 | BlockEncoding shall retain the scalar scaling factor of the encoded operator. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0371-02 | BlockEncoding shall retain a list of ancillary-variable templates. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0371-03 | When BlockEncoding.from_operator receives a QubitOperator or FermionicOperator, BlockEncoding shall create a BlockEncoding from that operator. | event_driven | Schnittstelle | nein | indirect |
| QR-0371-04 | When BlockEncoding.from_array receives a 2-D array, BlockEncoding shall create a BlockEncoding from the array. | event_driven | Schnittstelle | nein | indirect |
| QR-0371-05 | When two BlockEncoding instances are added, BlockEncoding shall encode the sum of their encoded operators. | event_driven | funktional/Leistung | nein | indirect |
| QR-0371-06 | When two BlockEncoding instances are multiplied, BlockEncoding shall encode the product of their encoded operators. | event_driven | funktional/Leistung | nein | indirect |
| QR-0371-07 | When reflection receives no state function, reflection shall perform a reflection around the \|0> state. | event_driven | Schnittstelle | nein | indirect |

#### PR 373

[github.com/eclipse-qrisp/Qrisp/pull/373](https://github.com/eclipse-qrisp/Qrisp/pull/373) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0373-01 | While tracing mode is active, mcz shall apply a multi-controlled Z operation using the specified control state. | state_driven | funktional/Leistung | nein | indirect |

#### PR 374

[github.com/eclipse-qrisp/Qrisp/pull/374](https://github.com/eclipse-qrisp/Qrisp/pull/374) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0374-01 | q_switch shall expose the interface q_switch(index, branches, *operands, branch_amount=None, method="auto"). | ubiquitous | Schnittstelle | nein | indirect |
| QR-0374-02 | When index is classical, q_switch shall execute branches[index] with the supplied operands. | event_driven | Schnittstelle | nein | indirect |
| QR-0374-03 | When index is a QuantumVariable or a list of Qubits, q_switch shall execute a quantum switch-case statement using the supplied branches and operands. | event_driven | Schnittstelle | nein | indirect |
| QR-0374-04 | When qswitch is called, qswitch shall issue a FutureWarning that directs users to q_switch. | event_driven | Schnittstelle | nein | indirect |

#### PR 377

[github.com/eclipse-qrisp/Qrisp/pull/377](https://github.com/eclipse-qrisp/Qrisp/pull/377) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0377-01 | Qrisp shall require jax version 0.7.1. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0377-02 | Qrisp shall require jaxlib version 0.7.1. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0377-03 | When an equation primitive has the name jit, Qrisp shall process the equation. | event_driven | funktional/Leistung | nein | indirect |
| QR-0377-04 | When constructing a Jaxpr from a QuantumEnvironment, Qrisp shall provide debug information to the Jaxpr constructor. | event_driven | Schnittstelle | nein | indirect |

#### PR 378

[github.com/eclipse-qrisp/Qrisp/pull/378](https://github.com/eclipse-qrisp/Qrisp/pull/378) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0378-01 | When a QuantumFloat is unsigned, q_fractional shall subtract the floor of the QuantumFloat from its fractional result. | event_driven | funktional/Leistung | nein | insufficient |

#### PR 379

[github.com/eclipse-qrisp/Qrisp/pull/379](https://github.com/eclipse-qrisp/Qrisp/pull/379) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0379-01 | BigInteger shall return the unsigned greater-than comparison result for the > operator. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0379-02 | BigInteger shall return the unsigned greater-or-equal comparison result for the >= operator. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 380

[github.com/eclipse-qrisp/Qrisp/pull/380](https://github.com/eclipse-qrisp/Qrisp/pull/380) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0380-01 | When optimizing a control pulse, DCQOProblem shall execute its optimization routine three times. | event_driven | funktional/Leistung | nein | indirect |
| QR-0380-02 | When choosing control-pulse parameters from three optimization runs, DCQOProblem shall select the parameter set with the lowest objective cost. | event_driven | funktional/Leistung | nein | indirect |
| QR-0380-03 | When callers omit sympy_g, DCQOProblem shall assign None to sympy_g. | event_driven | Schnittstelle | nein | indirect |
| QR-0380-04 | DCQOProblem.run shall default the bounds parameter to an empty tuple. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 381

[github.com/eclipse-qrisp/Qrisp/pull/381](https://github.com/eclipse-qrisp/Qrisp/pull/381) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0381-01 | solve_QUBO shall solve a QUBO matrix using counterdiabatic driving. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0381-02 | DCQOProblem shall return each measurement result with the QUBO cost for its bitstring. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0381-03 | create_COLD_instance shall return a COLD DCQO problem-initialization configuration derived from a QUBO matrix. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0381-04 | create_LCD_instance shall return an LCD DCQO problem-initialization configuration derived from a QUBO matrix. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 384

[github.com/eclipse-qrisp/Qrisp/pull/384](https://github.com/eclipse-qrisp/Qrisp/pull/384) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0384-01 | When a QuantumFloat is signed, QuantumFloat.encoder shall return the unsigned representation of the exponent-scaled signed input. | event_driven | Schnittstelle | nein | indirect |
| QR-0384-02 | When a QuantumFloat is unsigned, QuantumFloat.encoder shall return the input divided by 2 raised to the QuantumFloat exponent. | event_driven | Schnittstelle | nein | indirect |
| QR-0384-03 | When a QuantumFloat is signed, QuantumFloat.decoder shall return the exponent-scaled signed representation of the encoded integer. | event_driven | Schnittstelle | nein | indirect |
| QR-0384-04 | When a QuantumFloat is unsigned, QuantumFloat.decoder shall return the encoded integer multiplied by 2 raised to the QuantumFloat exponent. | event_driven | Schnittstelle | nein | indirect |

#### PR 389

[github.com/eclipse-qrisp/Qrisp/pull/389](https://github.com/eclipse-qrisp/Qrisp/pull/389) · 9 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0389-01 | cuccaro_adder shall modify the second input in place. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0389-02 | cuccaro_adder shall operate in static mode. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0389-03 | cuccaro_adder shall operate in dynamic mode. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0389-04 | cuccaro_adder shall accept two quantum inputs. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0389-05 | While the second input is quantum, cuccaro_adder shall accept a classical first input. | state_driven | Schnittstelle | nein | indirect |
| QR-0389-06 | When the first input is larger than the second input, cuccaro_adder shall truncate the first input to the second input's size before performing modulo addition relative to the second input's size. | event_driven | funktional/Leistung | nein | indirect |
| QR-0389-07 | When the control qubit is in the \|1> state, cuccaro_adder shall add the first input to the second input. | event_driven | funktional/Leistung | nein | indirect |
| QR-0389-08 | cuccaro_adder shall execute the addition truth table on input qubit arrays without applying input typing semantics. | ubiquitous | funktional/Leistung | nein | direct |
| QR-0389-09 | When cuccaro_procedure is called, cuccaro_procedure shall raise a RemovedFunctionError. | event_driven | Schnittstelle | nein | indirect |

#### PR 390

[github.com/eclipse-qrisp/Qrisp/pull/390](https://github.com/eclipse-qrisp/Qrisp/pull/390) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0390-01 | Jaspr.extract_post_processing shall return a callable that applies classical post-processing logic to measurement results. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0390-02 | When supplied with a string of '0' and '1' characters, the returned post-processing function shall return post-processed results for the measurement values. | event_driven | Schnittstelle | nein | indirect |
| QR-0390-03 | When supplied with a JAX boolean array, the returned post-processing function shall return post-processed results for the array's measurement values. | event_driven | Schnittstelle | nein | indirect |
| QR-0390-04 | While processing measurements, the returned post-processing function shall consume measurement results in chronological measurement order. | state_driven | funktional/Leistung | nein | indirect |
| QR-0390-05 | When supplied with static argument values used for circuit extraction, Jaspr.extract_post_processing shall bind the values into the returned post-processing function. | event_driven | Schnittstelle | nein | indirect |

#### PR 391

[github.com/eclipse-qrisp/Qrisp/pull/391](https://github.com/eclipse-qrisp/Qrisp/pull/391) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0391-01 | Qrisp shall require Python version 3.11 or later for installation. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 394

[github.com/eclipse-qrisp/Qrisp/pull/394](https://github.com/eclipse-qrisp/Qrisp/pull/394) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0394-01 | When compiling a quantum-controlled dynamic loop, Qrisp shall complete compilation without a compilation failure. | event_driven | funktional/Leistung | nein | indirect |

#### PR 398

[github.com/eclipse-qrisp/Qrisp/pull/398](https://github.com/eclipse-qrisp/Qrisp/pull/398) · 7 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0398-01 | q_ntt shall perform an in-place number-theoretic transform on x. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0398-02 | q_ntt_inv shall perform an in-place inverse number-theoretic transform on x. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0398-03 | q_multiply_ntt shall store the product of two NTT representations in result. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0398-04 | When r = t - A*s satisfies the coefficient-wise centered-magnitude bound B_e, create_lwe_oracle shall mark s. | event_driven | funktional/Leistung | nein | indirect |
| QR-0398-05 | run_lwe_grover_amplification shall apply amplitude amplification for the specified number of iterations. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0398-06 | Where other is a JAX ndarray, QuantumArray shall perform element-wise array injection. | optional_feature | Schnittstelle | nein | indirect |
| QR-0398-07 | Where other is a NumPy ndarray, QuantumArray shall perform element-wise array injection. | optional_feature | Schnittstelle | nein | indirect |

#### PR 399

[github.com/eclipse-qrisp/Qrisp/pull/399](https://github.com/eclipse-qrisp/Qrisp/pull/399) · 7 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0399-01 | When a jaspify-decorated function returns a PyTree, jaspify shall return the result with the function's original PyTree structure. | event_driven | funktional/Leistung | nein | indirect |
| QR-0399-02 | When a boolean_simulation-decorated function returns a PyTree, boolean_simulation shall return the result with the function's original PyTree structure. | event_driven | funktional/Leistung | nein | indirect |
| QR-0399-03 | When a qjit-decorated function returns a PyTree, qjit shall return the result with the function's original PyTree structure. | event_driven | funktional/Leistung | nein | indirect |
| QR-0399-04 | When return_shape=True is requested, make_jaxpr_mod shall return a ClosedJaxpr and a PyTreeDef representing the output structure. | event_driven | Schnittstelle | nein | indirect |
| QR-0399-05 | When return_shape=True is requested, make_jaspr shall return a Jaspr and a PyTreeDef representing the output structure. | event_driven | Schnittstelle | nein | indirect |
| QR-0399-06 | When a decorated function returns a quantum value, boolean_simulation shall raise an exception. | event_driven | funktional/Leistung | nein | indirect |
| QR-0399-07 | Qrisp documentation shall document make_jaspr. | ubiquitous | Prozess | nein | indirect |

#### PR 403

[github.com/eclipse-qrisp/Qrisp/pull/403](https://github.com/eclipse-qrisp/Qrisp/pull/403) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0403-01 | BlockEncoding 101 shall provide theory sufficient for a CS person to handle the BlockEncoding class. | ubiquitous | Prozess | nein | direct |
| QR-0403-02 | BlockEncoding 201 shall provide theory alongside examples showing how the theory is implemented in Qrisp. | ubiquitous | Prozess | nein | indirect |
| QR-0403-03 | When readers reach the end of BlockEncoding 201, BlockEncoding 201 shall refer readers to the filtering tutorial. | event_driven | Prozess | nein | indirect |
| QR-0403-04 | The filtering tutorial shall be usable as a standalone tutorial. | ubiquitous | Prozess | nein | indirect |

#### PR 404

[github.com/eclipse-qrisp/Qrisp/pull/404](https://github.com/eclipse-qrisp/Qrisp/pull/404) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0404-01 | While executing the COLD algorithm, DCQOProblem shall require an H_control control Hamiltonian. | state_driven | Schnittstelle | nein | direct |
| QR-0404-02 | While executing the COLD algorithm, DCQOProblem shall require a g_func inverse scheduling function. | state_driven | Schnittstelle | nein | direct |
| QR-0404-03 | When H_control is not given, DCQOProblem shall use the LCD method automatically. | event_driven | funktional/Leistung | nein | indirect |
| QR-0404-04 | When no qarg_prep function is specified, DCQOProblem shall leave the QuantumVariable in its initial state. | event_driven | funktional/Leistung | nein | indirect |
| QR-0404-05 | When solve_QUBO receives an LCD problem without an agp_type argument, solve_QUBO shall use order1 as the AGP type. | event_driven | Schnittstelle | nein | indirect |

#### PR 405

[github.com/eclipse-qrisp/Qrisp/pull/405](https://github.com/eclipse-qrisp/Qrisp/pull/405) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0405-01 | When a caller supplies a calibration_set_id, IQMBackend shall use the identified calibration set. | event_driven | Schnittstelle | nein | indirect |
| QR-0405-02 | When calibration_set_id is None, IQMBackend shall query the IQM Server for the current default calibration set. | event_driven | Schnittstelle | nein | indirect |
| QR-0405-03 | IQMBackend shall default use_metrics to False. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0405-04 | When use_metrics is True, IQMBackend shall query the server for calibration data and related quality metrics. | event_driven | funktional/Leistung | nein | indirect |
| QR-0405-05 | When use_metrics is True, IQMBackend shall pass calibration data and related quality metrics to the transpilation target(s). | event_driven | Schnittstelle | nein | indirect |

#### PR 406

[github.com/eclipse-qrisp/Qrisp/pull/406](https://github.com/eclipse-qrisp/Qrisp/pull/406) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0406-01 | num_qubits shall return the total number of qubits allocated during the computation. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0406-02 | num_qubits shall return the total number of qubits deallocated during the computation. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0406-03 | num_qubits shall return the peak number of qubits allocated during the computation. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0406-04 | num_qubits shall return the number of qubits still allocated at the end of the computation. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0406-05 | If the number of allocation or deallocation events exceeds max_allocations, then num_qubits shall raise a ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0406-06 | When qubits are created inside a conditional, depth shall calculate the circuit depth. | event_driven | funktional/Leistung | nein | indirect |

#### PR 408

[github.com/eclipse-qrisp/Qrisp/pull/408](https://github.com/eclipse-qrisp/Qrisp/pull/408) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0408-01 | Qrisp documentation shall clarify the bit-ordering conventions used across Qrisp. | ubiquitous | Prozess | nein | direct |

#### PR 409

[github.com/eclipse-qrisp/Qrisp/pull/409](https://github.com/eclipse-qrisp/Qrisp/pull/409) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0409-01 | When CKS receives a BlockEncoding, CKS shall return a BlockEncoding. | event_driven | Schnittstelle | nein | indirect |
| QR-0409-02 | When reflection is invoked without a state function, reflection shall perform a reflection around the \|0> state. | event_driven | Schnittstelle | nein | indirect |
| QR-0409-03 | GQET shall return a BlockEncoding representing a polynomial transformation of the input operator. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0409-04 | convolve shall perform cyclic convolution of a quantum state with a filter. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0409-05 | fourier_series_loader shall perform band-limited quantum state preparation. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 410

[github.com/eclipse-qrisp/Qrisp/pull/410](https://github.com/eclipse-qrisp/Qrisp/pull/410) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0410-01 | When a newer commit is pushed to a pull request while jobs for an earlier commit are running, the pipeline shall cancel the jobs for the earlier commit. | event_driven | Prozess | nein | indirect |

#### PR 411

[github.com/eclipse-qrisp/Qrisp/pull/411](https://github.com/eclipse-qrisp/Qrisp/pull/411) · 8 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0411-01 | The gidney_adder2 function shall add a to b in place. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0411-02 | The gidney_adder2 function shall accept an int as its a argument. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0411-03 | The gidney_adder2 function shall accept a QuantumVariable as its a argument. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0411-04 | The gidney_adder2 function shall accept a list[Qubit] as its a argument. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0411-05 | The gidney_adder2 function shall accept a QuantumVariable as its b argument. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0411-06 | The gidney_adder2 function shall accept a list[Qubit] as its b argument. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0411-07 | The gidney_adder2 function shall accept c_in as an optional Qubit argument. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0411-08 | The gidney_adder2 function shall accept c_out as an optional Qubit argument. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 413

[github.com/eclipse-qrisp/Qrisp/pull/413](https://github.com/eclipse-qrisp/Qrisp/pull/413) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0413-01 | QuantumCircuit.to_stim shall convert a Qrisp QuantumCircuit into a Stim circuit. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0413-02 | If a circuit contains a non-Clifford gate, then qrisp_to_stim shall raise an exception. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0413-03 | When a cache key composed of argument types, argument shapes, and measurement behavior is absent, function.jaspr_dict shall cache a Jaspr trace under that key. | event_driven | funktional/Leistung | nein | indirect |
| QR-0413-04 | extract_stim shall extract a Stim circuit from a Jasp-traceable function. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0413-05 | parity shall perform a parity check on measurement results. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 414

[github.com/eclipse-qrisp/Qrisp/pull/414](https://github.com/eclipse-qrisp/Qrisp/pull/414) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0414-01 | The function.jaspr_dict shall distinguish cached JASPRs used by count_ops according to argument shape. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0414-02 | The function.jaspr_dict shall distinguish cached JASPRs used by count_ops according to measurement behavior. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0414-03 | The function.jaspr_dict shall distinguish cached JASPRs used by depth according to argument shape. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0414-04 | The function.jaspr_dict shall distinguish cached JASPRs used by depth according to measurement behavior. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 415

[github.com/eclipse-qrisp/Qrisp/pull/415](https://github.com/eclipse-qrisp/Qrisp/pull/415) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0415-01 | When qswitch state preparation is followed by its inversion, prepare_qswitch shall restore the quantum register to its state before preparation. | event_driven | funktional/Leistung | nein | indirect |

#### PR 416

[github.com/eclipse-qrisp/Qrisp/pull/416](https://github.com/eclipse-qrisp/Qrisp/pull/416) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0416-01 | The DCQOProblem class shall solve digitized counterdiabatic quantum optimization problems with the LCD algorithm. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0416-02 | The DCQOProblem class shall solve digitized counterdiabatic quantum optimization problems with the COLD algorithm. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0416-03 | The solve_QUBO function shall execute COLD-CRAB QUBO runs. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0416-04 | The solve_QUBO function shall return a dictionary of QUBO vector results with probabilities and costs. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0416-05 | The tests shall verify that COLD method flavors run without errors. | ubiquitous | Prozess | nein | direct |

#### PR 421

[github.com/eclipse-qrisp/Qrisp/pull/421](https://github.com/eclipse-qrisp/Qrisp/pull/421) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0421-01 | While executing in static mode, when a value cannot be represented by a QuantumFloat, QuantumFloat shall raise a ValueError. | complex | Schnittstelle | nein | indirect |
| QR-0421-02 | While executing outside tracing mode, when encoding_number exceeds 2 ** len(qv) - 1, int_encoder shall raise a ValueError. | complex | Schnittstelle | nein | direct |

#### PR 424

[github.com/eclipse-qrisp/Qrisp/pull/424](https://github.com/eclipse-qrisp/Qrisp/pull/424) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0424-01 | When reconstructing a DynamicJaxArray from flattened data, DynamicJaxArray shall initialize its maximum size to the length of the flattened array. | event_driven | funktional/Leistung | nein | indirect |

#### PR 425

[github.com/eclipse-qrisp/Qrisp/pull/425](https://github.com/eclipse-qrisp/Qrisp/pull/425) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0425-01 | When no qarg_prep is specified, the DCQOProblem shall prepare the \|−⟩^n state. | event_driven | funktional/Leistung | nein | indirect |
| QR-0425-02 | The DCQOProblem documentation shall describe COLD as counterdiabatic optimized local driving. | ubiquitous | Prozess | nein | indirect |
| QR-0425-03 | The DCQOProblem documentation shall describe LCD as local counterdiabatic driving. | ubiquitous | Prozess | nein | indirect |
| QR-0425-04 | The DCQOProblem documentation shall link to publications for DCQO and COLD. | ubiquitous | Prozess | nein | direct |
| QR-0425-05 | Qrisp shall expose the cold module as qrisp.cold. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 426

[github.com/eclipse-qrisp/Qrisp/pull/426](https://github.com/eclipse-qrisp/Qrisp/pull/426) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0426-01 | The convolution shall use the Gidney adder as its default shift implementation. | ubiquitous | funktional/Leistung | nein | direct |

#### PR 427

[github.com/eclipse-qrisp/Qrisp/pull/427](https://github.com/eclipse-qrisp/Qrisp/pull/427) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0427-01 | The prepare docstring shall state that the qswitch method is incompatible with QuantumEnvironments in Jasp mode. | ubiquitous | Prozess | nein | indirect |
| QR-0427-02 | The prepare docstring shall state that the qswitch method cannot prepare a state with 64 or more qubits. | ubiquitous | Prozess | nein | indirect |

#### PR 428

[github.com/eclipse-qrisp/Qrisp/pull/428](https://github.com/eclipse-qrisp/Qrisp/pull/428) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0428-01 | The landing page shall display the official Eclipse white logo. | ubiquitous | Qualität (nicht funktional) | nein | direct |

#### PR 429

[github.com/eclipse-qrisp/Qrisp/pull/429](https://github.com/eclipse-qrisp/Qrisp/pull/429) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0429-01 | The Qrisp tutorial shall explain how to use the BigInteger class to avoid integer overflow in Jasp. | ubiquitous | Prozess | nein | indirect |
| QR-0429-02 | The Qrisp tutorial shall explain resource estimation of the order-finding quantum routine. | ubiquitous | Prozess | nein | indirect |
| QR-0429-03 | While executing its __call__ method in tracing mode, BigInteger shall return a float64 approximation of the integer value. | state_driven | Schnittstelle | nein | indirect |
| QR-0429-04 | While executing its __call__ method outside tracing mode, BigInteger shall return an exact Python integer. | state_driven | Schnittstelle | nein | indirect |

#### PR 431

[github.com/eclipse-qrisp/Qrisp/pull/431](https://github.com/eclipse-qrisp/Qrisp/pull/431) · 8 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0431-01 | Qrisp shall compile quantum algorithms expressed through its high-level programming constructs into executable quantum circuits. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0431-02 | When variables from different sessions interact, the automatic Session Merging system shall transparently unify the variables. | event_driven | funktional/Leistung | nein | indirect |
| QR-0431-03 | When slicing a QuantumArray, QuantumArray shall create a view without allocating additional qubits. | event_driven | funktional/Leistung | nein | indirect |
| QR-0431-04 | When reshaping a QuantumArray, QuantumArray shall create a view without allocating additional qubits. | event_driven | funktional/Leistung | nein | indirect |
| QR-0431-05 | When transposing a QuantumArray, QuantumArray shall create a view without allocating additional qubits. | event_driven | funktional/Leistung | nein | indirect |
| QR-0431-06 | When concatenating a QuantumArray, QuantumArray shall create a view without allocating additional qubits. | event_driven | funktional/Leistung | nein | indirect |
| QR-0431-07 | When compiling an infix arithmetic expression on quantum types, Qrisp shall compile the expression into a reversible circuit. | event_driven | funktional/Leistung | nein | indirect |
| QR-0431-08 | The auto_uncompute decorator shall reverse temporary quantum variables created during a decorated computation. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 432

[github.com/eclipse-qrisp/Qrisp/pull/432](https://github.com/eclipse-qrisp/Qrisp/pull/432) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0432-01 | Qrisp tutorials shall open hyperlink targets in new browser tabs. | ubiquitous | Gebrauchstauglichkeit | nein | indirect |
| QR-0432-02 | Qrisp tutorials shall display backtracking trees. | ubiquitous | Gebrauchstauglichkeit | nein | indirect |
| QR-0432-03 | When a caller supplies an axes object, visualize_statevector shall draw the statevector graph on the supplied axes object. | event_driven | Schnittstelle | nein | indirect |
| QR-0432-04 | When the index variable is in state \|i>, q_switch shall apply branch unitary U_i. | event_driven | funktional/Leistung | nein | indirect |

#### PR 433

[github.com/eclipse-qrisp/Qrisp/pull/433](https://github.com/eclipse-qrisp/Qrisp/pull/433) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0433-01 | When a fuse operation combines a quantum register with a single qubit, DepthMetric shall compute the circuit depth using the fused register. | event_driven | funktional/Leistung | nein | indirect |
| QR-0433-02 | If a slice operation produces a nonpositive slice size, then DepthMetric shall issue a warning identifying the supplied slice indices. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0433-03 | When a reset primitive is processed for the depth metric, DepthMetric shall issue a warning that reset is not implemented. | event_driven | funktional/Leistung | nein | indirect |

#### PR 434

[github.com/eclipse-qrisp/Qrisp/pull/434](https://github.com/eclipse-qrisp/Qrisp/pull/434) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0434-01 | Qrisp shall compile quantum programs into executable quantum circuits. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0434-02 | Qrisp shall output standard circuit objects. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0434-03 | When QuantumVariables from different sessions interact, the automatic Session Merging shall transparently unify the QuantumVariables' sessions. | event_driven | funktional/Leistung | nein | indirect |
| QR-0434-04 | QuantumArray shall provide slice operations without allocating additional qubits. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0434-05 | Qrisp shall compile infix arithmetic expressions on quantum types into reversible circuits. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0434-06 | The auto_uncompute decorator shall free the qubits of temporary quantum variables created during the decorated computation. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 435

[github.com/eclipse-qrisp/Qrisp/pull/435](https://github.com/eclipse-qrisp/Qrisp/pull/435) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0435-01 | AbstractQuantumState shall replace AbstractQuantumCircuit as the Jax abstract type. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 436

[github.com/eclipse-qrisp/Qrisp/pull/436](https://github.com/eclipse-qrisp/Qrisp/pull/436) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0436-01 | Qrisp shall display the HSRM logo. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 440

[github.com/eclipse-qrisp/Qrisp/pull/440](https://github.com/eclipse-qrisp/Qrisp/pull/440) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0440-01 | IQMBackend shall accept a Boolean use_timeslot parameter with a default value of False. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0440-02 | When submitting a circuit batch, IQMBackend shall pass its use_timeslot parameter value to IQMClient. | event_driven | Schnittstelle | nein | indirect |

#### PR 441

[github.com/eclipse-qrisp/Qrisp/pull/441](https://github.com/eclipse-qrisp/Qrisp/pull/441) · 9 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0441-01 | The Version history shall include Qrisp 0.8. | ubiquitous | Prozess | nein | indirect |
| QR-0441-02 | BlockEncoding.from_array shall construct a BlockEncoding from a NumPy array. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0441-03 | BlockEncoding.from_operator shall encode a Hamiltonian as a BlockEncoding. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0441-04 | BlockEncoding.from_lcu shall construct a BlockEncoding from a weighted sum of unitaries. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0441-05 | GQSP shall apply a complex polynomial p(z) to a unitary U. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0441-06 | When converting a Jaspr to MLIR, Jaspr.to_mlir shall return an xDSL ModuleOp. | event_driven | Schnittstelle | nein | indirect |
| QR-0441-07 | When tracing a Qrisp function, extract_stim shall convert the function to a Stim circuit. | event_driven | Schnittstelle | nein | indirect |
| QR-0441-08 | parity shall compute the XOR parity of measurement results. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0441-09 | find_detectors shall identify detector instructions using tqecd. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 442

[github.com/eclipse-qrisp/Qrisp/pull/442](https://github.com/eclipse-qrisp/Qrisp/pull/442) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0442-01 | When qq_montgomery_multiply_modulus multiplies QuantumModulus operands with a shared modulus and arbitrary Montgomery shifts, qq_montgomery_multiply_modulus shall return their product modulo the shared modulus. | event_driven | funktional/Leistung | nein | indirect |
| QR-0442-02 | When both qq_montgomery_multiply_modulus inputs are in standard form with m=0, qq_montgomery_multiply_modulus shall return a result in standard form. | event_driven | funktional/Leistung | nein | indirect |
| QR-0442-03 | If QuantumModulus operands have differing moduli, then qq_montgomery_multiply_modulus shall raise an exception. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0442-04 | When a QuantumModulus Montgomery shift m is negative, jdecoder shall return i multiplied by 2 to the power of -m modulo the QuantumModulus modulus. | event_driven | funktional/Leistung | nein | indirect |
| QR-0442-05 | When R is a float strictly between zero and one, montgomery_decoder shall return y multiplied modulo N by int(R raised to -1). | event_driven | funktional/Leistung | nein | indirect |

#### PR 443

[github.com/eclipse-qrisp/Qrisp/pull/443](https://github.com/eclipse-qrisp/Qrisp/pull/443) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0443-01 | The Tutorial landing page shall categorize tutorials as Foundations and first Steps, Optimization and numerics, High-Performance execution and compilation (Jasp), and Scientific computing and quantum numerical linear algebra. | ubiquitous | Gebrauchstauglichkeit | nein | indirect |

#### PR 444

[github.com/eclipse-qrisp/Qrisp/pull/444](https://github.com/eclipse-qrisp/Qrisp/pull/444) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0444-01 | The Algorithms documentation landing page shall classify algorithm listings under the Foundational Algorithms, Combinatorial Optimization, and Chemistry, Physics and Scientific Computing sections. | ubiquitous | Prozess | nein | indirect |

#### PR 445

[github.com/eclipse-qrisp/Qrisp/pull/445](https://github.com/eclipse-qrisp/Qrisp/pull/445) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0445-01 | The vdot method shall return the scalar result of sparse matrix multiplication. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 448

[github.com/eclipse-qrisp/Qrisp/pull/448](https://github.com/eclipse-qrisp/Qrisp/pull/448) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0448-01 | The BlockEncoding class shall construct nested commutators of BlockEncoding instances. | ubiquitous | funktional/Leistung | nein | direct |
| QR-0448-02 | The BlockEncoding class shall provide an einsum-equivalent operation that performs arbitrary tensor contraction. | ubiquitous | Schnittstelle | nein | direct |
| QR-0448-03 | The BlockEncoding class shall generate custom block encodings for N-dimensional finite-difference Laplacian discretizations. | ubiquitous | funktional/Leistung | nein | direct |

#### PR 450

[github.com/eclipse-qrisp/Qrisp/pull/450](https://github.com/eclipse-qrisp/Qrisp/pull/450) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0450-01 | BlockEncoding shall expose the `from_operator` method. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 451

[github.com/eclipse-qrisp/Qrisp/pull/451](https://github.com/eclipse-qrisp/Qrisp/pull/451) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0451-01 | When processing a reset operation, the depth profiler shall omit the not-implemented warning. | event_driven | funktional/Leistung | nein | indirect |
| QR-0451-02 | When processing a delete-qubits operation, the depth profiler shall omit the not-implemented warning. | event_driven | funktional/Leistung | nein | indirect |
| QR-0451-03 | The depth metric shall document that it is experimental and may not behave as expected in certain edge cases. | ubiquitous | Schnittstelle | nein | direct |
| QR-0451-04 | The depth metric shall document that reset and delete memory-management operations are ignored. | ubiquitous | Schnittstelle | nein | direct |
| QR-0451-05 | The depth metric shall document that qubits freed by reset and delete operations count toward the max_qubits limit. | ubiquitous | Schnittstelle | nein | direct |
| QR-0451-06 | The depth metric shall document that it handles a slice operation correctly only when the lower slice bound is strictly smaller than the upper slice bound. | ubiquitous | Schnittstelle | nein | direct |

#### PR 452

[github.com/eclipse-qrisp/Qrisp/pull/452](https://github.com/eclipse-qrisp/Qrisp/pull/452) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0452-01 | BaseMetric shall initialize with meas_behavior without requiring profiling_dic. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0452-02 | BaseMetric shall require metric implementations to provide an initial metric value. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0452-03 | BaseMetric shall require metric implementations to provide a cache key for their configurations. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0452-04 | BaseMetric shall require metric implementations to reconstruct instances from cache keys. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0452-05 | When computing depth for a sliced quantum register, DepthMetric shall apply Python semantics to slice start and stop bounds. | event_driven | funktional/Leistung | nein | indirect |

#### PR 453

[github.com/eclipse-qrisp/Qrisp/pull/453](https://github.com/eclipse-qrisp/Qrisp/pull/453) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0453-01 | The custom_inversion decorator shall require decorated functions to accept an inv keyword argument that receives a static Boolean value. | ubiquitous | Schnittstelle | nein | direct |
| QR-0453-02 | When a decorated function is called within an InversionEnvironment, the custom_inversion decorator shall automatically invoke the decorated function's backward version. | event_driven | funktional/Leistung | nein | indirect |
| QR-0453-03 | The custom_inversion decorator shall make custom inversion available only in dynamic mode. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0453-04 | The InversionEnvironment documentation shall include an API reference for custom_inversion. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 457

[github.com/eclipse-qrisp/Qrisp/pull/457](https://github.com/eclipse-qrisp/Qrisp/pull/457) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0457-01 | While q is prime, n divides q-1, and root is an n-th root of unity modulo q, q_ntt shall perform an in-place number theoretic transform on x. | state_driven | funktional/Leistung | nein | indirect |
| QR-0457-02 | q_multiply_ntt shall compute the product of two NTT representations. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0457-03 | When a candidate s produces r = t - A*s whose coefficients each have centered magnitude no greater than B_e, the LWE oracle shall mark s. | event_driven | funktional/Leistung | nein | indirect |
| QR-0457-04 | run_lwe_grover_amplification shall return a QuantumArray after applying amplitude amplification. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 459

[github.com/eclipse-qrisp/Qrisp/pull/459](https://github.com/eclipse-qrisp/Qrisp/pull/459) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0459-01 | If BigInteger.create_static receives a negative input, then BigInteger.create_static shall raise a ValueError stating that the input must be non-negative. | unwanted_behaviour | Schnittstelle | nein | indirect |

#### PR 461

[github.com/eclipse-qrisp/Qrisp/pull/461](https://github.com/eclipse-qrisp/Qrisp/pull/461) · 7 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0461-01 | When num_qubits is not an int, QuantumCircuit shall raise a TypeError. | event_driven | Schnittstelle | nein | indirect |
| QR-0461-02 | When num_clbits is not an int, QuantumCircuit shall raise a TypeError. | event_driven | Schnittstelle | nein | indirect |
| QR-0461-03 | QuantumCircuit.extend shall append instructions from another QuantumCircuit to the current QuantumCircuit. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0461-04 | QuantumCircuit.extend shall accept a translation dictionary with source-circuit bits as keys and destination-circuit bits as values. | ubiquitous | Schnittstelle | nein | direct |
| QR-0461-05 | When translation_dic is None, QuantumCircuit.extend shall use identity mapping based on matching identifiers. | event_driven | Schnittstelle | nein | indirect |
| QR-0461-06 | If a translated instruction references a qubit absent from the destination circuit, then QuantumCircuit.extend shall raise an exception. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0461-07 | If a translated instruction references a classical bit absent from the destination circuit, then QuantumCircuit.extend shall raise a ValueError. | unwanted_behaviour | funktional/Leistung | nein | indirect |

#### PR 464

[github.com/eclipse-qrisp/Qrisp/pull/464](https://github.com/eclipse-qrisp/Qrisp/pull/464) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0464-01 | When performing an exponentiation-by-squaring iteration, the factoring (Shor's algorithm) demo shall square the exponentiation base modulo N after the controlled multiplication. | event_driven | funktional/Leistung | nein | indirect |

#### PR 465

[github.com/eclipse-qrisp/Qrisp/pull/465](https://github.com/eclipse-qrisp/Qrisp/pull/465) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0465-01 | The JASP quantum dialect shall represent JASP operations as typed operations. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0465-02 | When Qrisp emits MLIR containing JASP types, the JASP quantum dialect shall print the type names without surrounding quotes. | event_driven | Schnittstelle | nein | indirect |
| QR-0465-03 | When Qrisp emits MLIR containing JASP operations, the JASP quantum dialect shall print the operation names without surrounding quotes. | event_driven | Schnittstelle | nein | indirect |
| QR-0465-04 | The CreateQubitsOp shall return a QuantumState output. | ubiquitous | Schnittstelle | nein | direct |
| QR-0465-05 | When a MeasureOp receives a QubitArray, the MeasureOp shall require the measurement-result type Tensor<int64>. | event_driven | Schnittstelle | nein | direct |
| QR-0465-06 | When a MeasureOp receives a Qubit, the MeasureOp shall require the measurement-result type Tensor<int1>. | event_driven | Schnittstelle | nein | direct |

#### PR 473

[github.com/eclipse-qrisp/Qrisp/pull/473](https://github.com/eclipse-qrisp/Qrisp/pull/473) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0473-01 | If an input pair is neither classical-quantum nor quantum-quantum, then _validate_gidney_adder_inputs shall raise ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0473-02 | While executing a QCLA adder within a QuantumEnvironment, the QCLA adder shall execute its operations within that QuantumEnvironment. | state_driven | funktional/Leistung | nein | direct |
| QR-0473-03 | The documentation for jrange shall state that continue does not work with jrange. | ubiquitous | Prozess | nein | direct |

#### PR 474

[github.com/eclipse-qrisp/Qrisp/pull/474](https://github.com/eclipse-qrisp/Qrisp/pull/474) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0474-01 | When installing test dependencies, the qrisp_test workflow shall install the gast package. | event_driven | Prozess | nein | indirect |

#### PR 475

[github.com/eclipse-qrisp/Qrisp/pull/475](https://github.com/eclipse-qrisp/Qrisp/pull/475) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0475-01 | The qrisp_test.yml workflow shall use actions/checkout@v5. | ubiquitous | Prozess | nein | indirect |
| QR-0475-02 | The qrisp_test.yml workflow shall use actions/setup-python@v6. | ubiquitous | Prozess | nein | indirect |

#### PR 477

[github.com/eclipse-qrisp/Qrisp/pull/477](https://github.com/eclipse-qrisp/Qrisp/pull/477) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0477-01 | When q_switch is invoked with multiple operands, q_switch shall invoke the index-selected branch with the supplied operands. | event_driven | funktional/Leistung | nein | indirect |

#### PR 478

[github.com/eclipse-qrisp/Qrisp/pull/478](https://github.com/eclipse-qrisp/Qrisp/pull/478) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0478-01 | When make_jaspr receives static_argnums in integer, tuple, or list form, make_jaspr shall create a JASPR containing six equations for main invoked with 2 and 3. | event_driven | Schnittstelle | nein | indirect |

#### PR 479

[github.com/eclipse-qrisp/Qrisp/pull/479](https://github.com/eclipse-qrisp/Qrisp/pull/479) · 9 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0479-01 | GQSVT shall return a BlockEncoding representing the selected parity polynomial transformation of a block-encoded operator. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0479-02 | When method is "GQSVT", inversion shall return a BlockEncoding approximating the inverse using Generalized Quantum Singular Value Transform. | event_driven | Schnittstelle | nein | indirect |
| QR-0479-03 | When method is "QET", inversion shall operate only on Hermitian block-encoded matrices. | event_driven | Schnittstelle | nein | indirect |
| QR-0479-04 | When its returned BlockEncoding is applied to operands in state \|0>, dalzell_inversion shall prepare a state proportional to A^{-1}\|b> within target precision epsilon. | event_driven | funktional/Leistung | nein | indirect |
| QR-0479-05 | pseudo_inversion shall return a BlockEncoding approximating the threshold matrix pseudoinverse of the supplied operator. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0479-06 | When given a diagonal index, BlockEncoding.from_eye shall return a BlockEncoding representing an array with ones on that diagonal and zeros elsewhere. | event_driven | Schnittstelle | nein | indirect |
| QR-0479-07 | When supplied left and right states, BlockEncoding.from_projector shall return a BlockEncoding representing the projector \|left><right\|. | event_driven | Schnittstelle | nein | indirect |
| QR-0479-08 | When kernel is True, BlockEncoding.from_projector shall return a BlockEncoding of I - \|phi><phi\|. | event_driven | Schnittstelle | nein | indirect |
| QR-0479-09 | If chebyshev_approx cannot converge to the requested tolerance within max_N, then chebyshev_approx shall issue a warning recommending an increased max_N. | unwanted_behaviour | Schnittstelle | nein | indirect |

#### PR 480

[github.com/eclipse-qrisp/Qrisp/pull/480](https://github.com/eclipse-qrisp/Qrisp/pull/480) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0480-01 | When invoked, cks_coeffs shall calculate coefficients efficiently. | event_driven | funktional/Leistung | nein | indirect |
| QR-0480-02 | When invoked with very large parameter values, cks_coeffs shall calculate numerically stable CKS coefficients. | event_driven | funktional/Leistung | nein | indirect |

#### PR 481

[github.com/eclipse-qrisp/Qrisp/pull/481](https://github.com/eclipse-qrisp/Qrisp/pull/481) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0481-01 | The probabilistic VQE tests shall assert that the absolute difference between the minimum H2 result and -1.85238817356958 is less than 3e-1. | ubiquitous | Prozess | nein | indirect |
| QR-0481-02 | The probabilistic VQE tests shall assert that the absolute difference between the minimum result and -8.0 is less than 2. | ubiquitous | Prozess | nein | indirect |

#### PR 482

[github.com/eclipse-qrisp/Qrisp/pull/482](https://github.com/eclipse-qrisp/Qrisp/pull/482) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0482-01 | GQSVT shall return a BlockEncoding of V p_odd(Σ) U† for odd-parity polynomial transformation. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0482-02 | GQSVT shall return a BlockEncoding of V p_even(Σ) V† for even-parity polynomial transformation. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0482-03 | pseudo_inversion shall return a BlockEncoding approximating the threshold pseudo inverse with error no greater than eps. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0482-04 | When method is "GQSVT", inversion shall return a BlockEncoding approximating the inverse of the block-encoded matrix with error no greater than eps. | event_driven | Schnittstelle | nein | indirect |
| QR-0482-05 | BlockEncoding.from_projector shall return a BlockEncoding representing the projector \|φ⟩⟨ψ\|. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0482-06 | chebyshev_approx shall return a truncated Chebyshev polynomial whose maximum truncation error is below eps. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 483

[github.com/eclipse-qrisp/Qrisp/pull/483](https://github.com/eclipse-qrisp/Qrisp/pull/483) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0483-01 | When invoked with a Jaxpr expression tree, analyze_call_graph shall provide a dictionary keyed by Jaxpr identity containing call-count, local-equation-count, and inlined-equation-count statistics for encountered sub-Jaxprs. | event_driven | Schnittstelle | nein | indirect |
| QR-0483-02 | When a sub-Jaxpr has a call count of at least two, an inlined equation count greater than 100, and operates on quantum state, _should_use_callback shall return True. | event_driven | funktional/Leistung | nein | indirect |

#### PR 484

[github.com/eclipse-qrisp/Qrisp/pull/484](https://github.com/eclipse-qrisp/Qrisp/pull/484) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0484-01 | When invoked with parity "odd", GQSVT shall return a BlockEncoding of V p_odd(Σ) U†. | event_driven | funktional/Leistung | nein | indirect |
| QR-0484-02 | When invoked with parity "even", GQSVT shall return a BlockEncoding of V p_even(Σ) V†. | event_driven | funktional/Leistung | nein | indirect |
| QR-0484-03 | When method is "GQSVT", inversion shall return a BlockEncoding whose represented operator approximates A⁻¹ with error no greater than ε. | event_driven | Schnittstelle | nein | indirect |
| QR-0484-04 | When applied to operands in state \|0⟩, dalzell_inversion shall prepare a state proportional to A⁻¹\|b⟩ within target precision ε. | event_driven | funktional/Leistung | nein | indirect |
| QR-0484-05 | When kernel is false, BlockEncoding.from_projector shall return a BlockEncoding representing \|φ⟩⟨ψ\|. | event_driven | Schnittstelle | nein | indirect |
| QR-0484-06 | When kernel is true, BlockEncoding.from_projector shall return a BlockEncoding representing I − \|φ⟩⟨φ\|. | event_driven | Schnittstelle | nein | indirect |

#### PR 485

[github.com/eclipse-qrisp/Qrisp/pull/485](https://github.com/eclipse-qrisp/Qrisp/pull/485) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0485-01 | When an injected function has no quantum argument, Function injection shall inject the function's returned quantum value into the target. | event_driven | Schnittstelle | nein | indirect |

#### PR 486

[github.com/eclipse-qrisp/Qrisp/pull/486](https://github.com/eclipse-qrisp/Qrisp/pull/486) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0486-01 | When add_clbit is called, QuantumCircuit shall increment clbit_index_counter. | event_driven | funktional/Leistung | nein | indirect |
| QR-0486-02 | If add_qubit receives a value that is not a Qubit, then QuantumCircuit shall raise TypeError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0486-03 | If add_clbit receives a value that is not a Clbit, then QuantumCircuit shall raise TypeError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0486-04 | If add_clbit receives a Clbit whose identifier is already present, then QuantumCircuit shall raise ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0486-05 | If to_gate is called on a circuit containing classical bits, then QuantumCircuit shall raise ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0486-06 | QuantumCircuit.get_unitary shall use None as its default argument. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 488

[github.com/eclipse-qrisp/Qrisp/pull/488](https://github.com/eclipse-qrisp/Qrisp/pull/488) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0488-01 | The Ruff configuration shall limit Python source lines to 120 characters. | ubiquitous | Prozess | nein | indirect |
| QR-0488-02 | The Ruff configuration shall select import sorting, pycodestyle, pydocstyle, pylint, and pyflakes lint rule sets. | ubiquitous | Prozess | nein | indirect |

#### PR 489

[github.com/eclipse-qrisp/Qrisp/pull/489](https://github.com/eclipse-qrisp/Qrisp/pull/489) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0489-01 | When bind_parameters creates a result circuit, QuantumCircuit shall initialize the result circuit's abstract_params as an empty set. | event_driven | Schnittstelle | nein | indirect |
| QR-0489-02 | When to_qasm2 encounters gates not representable in QASM 2.0, QuantumCircuit shall export the transpiled circuit. | event_driven | Schnittstelle | nein | indirect |
| QR-0489-03 | When measure receives an iterable of qubits other than a Qubit or int, QuantumCircuit shall allocate one Clbit per qubit. | event_driven | Schnittstelle | nein | indirect |
| QR-0489-04 | When parity receives a sequence of classical bits, QuantumCircuit shall treat the sequence as multi-clbit input. | event_driven | Schnittstelle | nein | indirect |
| QR-0489-05 | While xla_mode is less than 2, QuantumCircuit.add_clbit shall skip duplicate-identifier checking. | state_driven | Schnittstelle | nein | indirect |

#### PR 494

[github.com/eclipse-qrisp/Qrisp/pull/494](https://github.com/eclipse-qrisp/Qrisp/pull/494) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0494-01 | The `run_func` shall specify `None` as the default value of its `shots` parameter. | ubiquitous | Schnittstelle | nein | direct |
| QR-0494-02 | When the `shots` argument is `None`, the `run_func` shall substitute a default value for `shots`. | event_driven | Schnittstelle | nein | direct |

#### PR 495

[github.com/eclipse-qrisp/Qrisp/pull/495](https://github.com/eclipse-qrisp/Qrisp/pull/495) · 16 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0495-01 | When QuantumModulus inputs use arbitrary Montgomery shifts, qq_montgomery_multiply_modulus shall compute their Montgomery product with the resulting shift equal to x.m + y.m minus the reduction shift. | event_driven | funktional/Leistung | nein | indirect |
| QR-0495-02 | When cq_montgomery_multiply creates its result, cq_montgomery_multiply shall return a QuantumModulus. | event_driven | Schnittstelle | nein | indirect |
| QR-0495-03 | During JAX tracing, QuantumModulus.decoder shall decode Montgomery values with BigInteger moduli and traced Montgomery shifts. | state_driven | funktional/Leistung | nein | indirect |
| QR-0495-04 | When a non-tracing QuantumModulus.decoder receives a value greater than or equal to its modulus, QuantumModulus.decoder shall return nan. | event_driven | funktional/Leistung | nein | indirect |
| QR-0495-05 | When multiple raw basis states decode to the same classical value, decoded measurement handling shall accumulate their probabilities. | event_driven | funktional/Leistung | nein | indirect |
| QR-0495-06 | When QuantumModulus arithmetic receives a cached traced operand that is neither a QuantumModulus nor a QuantumFloat, QuantumModulus shall reduce the operand modulo its modulus before arithmetic. | event_driven | funktional/Leistung | nein | indirect |
| QR-0495-07 | When delete verification finds a dirty qubit, the classical function interpreter shall reset the qubit state before returning the qubit to the free pool. | event_driven | funktional/Leistung | nein | indirect |
| QR-0495-08 | When recursive_qs_search receives a QuantumVariable, recursive_qs_search shall treat the QuantumVariable as a leaf. | event_driven | funktional/Leistung | nein | indirect |
| QR-0495-09 | When BigInteger.coerce receives a BigInteger with fewer limbs than the requested size, BigInteger.coerce shall zero-pad the value to the requested size. | event_driven | Schnittstelle | nein | indirect |
| QR-0495-10 | When BigInteger.coerce receives a BigInteger with more limbs than the requested size, BigInteger.coerce shall raise a ValueError. | event_driven | Schnittstelle | nein | indirect |
| QR-0495-11 | When an integer is the dividend of a modulo operation with a BigInteger divisor, BigInteger.__rmod__ shall return the BigInteger remainder. | event_driven | Schnittstelle | nein | indirect |
| QR-0495-12 | When jasp_balauca_mcx receives a BigInteger ctrl_state, jasp_balauca_mcx shall use the BigInteger control-state representation. | event_driven | Schnittstelle | nein | indirect |
| QR-0495-13 | When Jaspr.copy copies a Jaspr with constants, Jaspr.copy shall preserve the constants in the copy. | event_driven | funktional/Leistung | nein | indirect |
| QR-0495-14 | When multi_control_jaspr constructs a controlled wrapper, multi_control_jaspr shall keep captured constants out of the wrapper's public runtime signature. | event_driven | Schnittstelle | nein | indirect |
| QR-0495-15 | When _moduli_neq receives a modulus containing JAX tracers, _moduli_neq shall raise a RuntimeError. | event_driven | funktional/Leistung | nein | indirect |
| QR-0495-16 | When measure_to_big_integer stores a measured limb, measure_to_big_integer shall store the limb as an unsigned 32-bit value. | event_driven | funktional/Leistung | nein | indirect |

#### PR 497

[github.com/eclipse-qrisp/Qrisp/pull/497](https://github.com/eclipse-qrisp/Qrisp/pull/497) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0497-01 | The _inlft function shall compile in constant time with respect to polynomial degree. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0497-02 | The gqsp_angles function shall calculate angles for a polynomial of degree 100,000 in less than 1 second. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 505

[github.com/eclipse-qrisp/Qrisp/pull/505](https://github.com/eclipse-qrisp/Qrisp/pull/505) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0505-01 | The boolean_simulation decorator shall accept an optional callback_threshold parameter with a default value of None. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0505-02 | The count_ops decorator shall accept an optional callback_threshold parameter with a default value of None. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0505-03 | The depth decorator shall accept an optional callback_threshold parameter with a default value of None. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0505-04 | The num_qubits decorator shall accept an optional callback_threshold parameter with a default value of None. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0505-05 | When callback_threshold is set and a reused sub-jaxpr's call_count multiplied by its inlined_eqn_count reaches the threshold, the profiling interpreter shall prevent XLA from duplicating the sub-jaxpr's HLO at call sites. | event_driven | funktional/Leistung | nein | indirect |
| QR-0505-06 | When callback wrapping is enabled, callback wrapping shall preserve the evaluation result. | event_driven | funktional/Leistung | nein | direct |

#### PR 517

[github.com/eclipse-qrisp/Qrisp/pull/517](https://github.com/eclipse-qrisp/Qrisp/pull/517) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0517-01 | The logo slider shall display logos in the "Trusted by" category. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0517-02 | The logo track shall continuously scroll the displayed logos. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0517-03 | When a user hovers over the logo track, the logo track shall pause its scrolling animation. | event_driven | funktional/Leistung | nein | indirect |

#### PR 518

[github.com/eclipse-qrisp/Qrisp/pull/518](https://github.com/eclipse-qrisp/Qrisp/pull/518) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0518-01 | The GitHub issue templates shall use `.github/ISSUE_TEMPLATE/` as their repository path. | ubiquitous | Schnittstelle | nein | direct |
| QR-0518-02 | The Bug Report issue template shall provide a bug-reporting form. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0518-03 | The Change Request issue template shall provide a form for proposing a change to existing Qrisp functionality. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0518-04 | The Documentation issue template shall provide a documentation-change form. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0518-05 | The Epic issue template shall provide a form for tracking a larger initiative with multiple sub-issues. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0518-06 | The Feature Request issue template shall provide a form for proposing a new Qrisp feature. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 519

[github.com/eclipse-qrisp/Qrisp/pull/519](https://github.com/eclipse-qrisp/Qrisp/pull/519) · 17 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0519-01 | The QuantumArray shall perform element-wise addition. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0519-02 | The QuantumArray shall perform element-wise subtraction. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0519-03 | The QuantumArray shall perform element-wise multiplication. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0519-04 | The QuantumArray shall perform element-wise equality comparison. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0519-05 | The QuantumArray shall perform element-wise inequality comparison. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0519-06 | The QuantumArray shall perform element-wise greater-than comparison. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0519-07 | The QuantumArray shall perform element-wise greater-than-or-equal comparison. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0519-08 | The QuantumArray shall perform element-wise less-than comparison. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0519-09 | The QuantumArray shall perform element-wise less-than-or-equal comparison. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0519-10 | The QuantumArray shall perform element-wise bitwise AND for QuantumBool arrays. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0519-11 | The QuantumArray shall perform element-wise bitwise OR for QuantumBool arrays. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0519-12 | The QuantumArray shall perform element-wise bitwise XOR for QuantumBool arrays. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0519-13 | The QuantumArray shall perform element-wise in-place addition. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0519-14 | The QuantumArray shall perform element-wise in-place subtraction. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0519-15 | The QuantumArray shall perform element-wise in-place multiplication. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0519-16 | When all is called with an axis, the QuantumArray shall apply a logical AND reduction over that axis to QuantumBool elements. | event_driven | funktional/Leistung | nein | indirect |
| QR-0519-17 | When any is called with an axis, the QuantumArray shall apply a logical OR reduction over that axis to QuantumBool elements. | event_driven | funktional/Leistung | nein | indirect |

#### PR 523

[github.com/eclipse-qrisp/Qrisp/pull/523](https://github.com/eclipse-qrisp/Qrisp/pull/523) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0523-01 | When QuantumFloat.encoder receives a value returned by QuantumFloat.decoder, QuantumFloat.encoder shall return the measurement outcome integer passed to QuantumFloat.decoder. | event_driven | funktional/Leistung | nein | indirect |
| QR-0523-02 | While in static mode, when QuantumFloat.encoder receives a negative value for an unsigned QuantumFloat, QuantumFloat.encoder shall raise a ValueError. | complex | funktional/Leistung | nein | indirect |
| QR-0523-03 | While in static mode, when QuantumFloat.encoder receives a value outside the QuantumFloat representable range, QuantumFloat.encoder shall raise a ValueError. | complex | funktional/Leistung | nein | indirect |

#### PR 526

[github.com/eclipse-qrisp/Qrisp/pull/526](https://github.com/eclipse-qrisp/Qrisp/pull/526) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0526-01 | When QuantumCircuit.r receives positional theta and phi values, QuantumCircuit.r shall treat theta as the first value and phi as the second value. | event_driven | Schnittstelle | nein | indirect |
| QR-0526-02 | When QuantumCircuit.barrier receives a clbits argument, QuantumCircuit.barrier shall raise a TypeError. | event_driven | Schnittstelle | nein | indirect |
| QR-0526-03 | The standard_operations module shall provide NumPy-style docstrings for standard-operation factory functions. | ubiquitous | Prozess | nein | indirect |

#### PR 528

[github.com/eclipse-qrisp/Qrisp/pull/528](https://github.com/eclipse-qrisp/Qrisp/pull/528) · 7 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0528-01 | Jaspr.to_mlir shall accept an optional lower_stablehlo Boolean parameter whose default is False. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0528-02 | When lower_stablehlo is True, Jaspr.to_mlir shall lower StableHLO arithmetic and data operations to linalg, arith, and tensor dialects. | event_driven | funktional/Leistung | nein | indirect |
| QR-0528-03 | When lower_stablehlo is False, Jaspr.to_mlir shall preserve StableHLO operations in emitted MLIR. | event_driven | funktional/Leistung | nein | indirect |
| QR-0528-04 | When emitted StableHLO control flow involves quantum types, Jaspr.to_mlir shall rewrite the control flow to SCF. | event_driven | funktional/Leistung | nein | indirect |
| QR-0528-05 | When a zero-dimensional linalg.generic operation produces one output tensor, scalar_linalg_folding shall replace the operation with an equivalent scalar-operation sequence. | event_driven | funktional/Leistung | nein | indirect |
| QR-0528-06 | When tensor.extract reads a zero-dimensional tensor.from_elements operation with one element, scalar_tensor_folding shall replace the extract result with the original scalar. | event_driven | funktional/Leistung | nein | indirect |
| QR-0528-07 | When an arith.cmpi operation compares a zero-extended Boolean to 0 or 1, FoldCmpiExtui shall replace the comparison with the equivalent Boolean condition or Boolean constant. | event_driven | funktional/Leistung | nein | indirect |

#### PR 532

[github.com/eclipse-qrisp/Qrisp/pull/532](https://github.com/eclipse-qrisp/Qrisp/pull/532) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0532-01 | When a push changes a file matching documentation/classes/*.docx, the Convert DOCX workflow shall execute DOCX conversion. | event_driven | Prozess | nein | indirect |
| QR-0532-02 | When a class inherits from BaseMetric, BaseMetric shall require the subclass to define an initial_metric property specifying the metric's initial value before quantum primitives execute. | event_driven | Schnittstelle | nein | direct |

#### PR 533

[github.com/eclipse-qrisp/Qrisp/pull/533](https://github.com/eclipse-qrisp/Qrisp/pull/533) · 11 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0533-01 | The Qrisp documentation shall link from the main documentation page to the Contributing Guide. | ubiquitous | Gebrauchstauglichkeit | nein | indirect |
| QR-0533-02 | Qrisp shall require Python 3.11 or later. | ubiquitous | Qualität (nicht funktional) | nein | indirect |
| QR-0533-03 | While a breaking change has not been explicitly agreed on with the maintainers, Qrisp contributions shall preserve existing user-facing behaviour. | state_driven | Prozess | nein | direct |
| QR-0533-04 | Before submitting a pull request, Qrisp contributors shall use a static-analysis tool to catch common issues. | event_driven | Prozess | nein | direct |
| QR-0533-05 | When a contribution adds or modifies public functionality, Qrisp contributions shall include corresponding documentation updates. | event_driven | Prozess | nein | direct |
| QR-0533-06 | When documenting a public function or class, Qrisp documentation shall use NumPy-style sectioned docstrings. | event_driven | Prozess | nein | direct |
| QR-0533-07 | When a docstring includes an Examples block, Qrisp documentation shall ensure that the Examples block executes correctly. | event_driven | Prozess | nein | indirect |
| QR-0533-08 | When a documentation page is added, Qrisp documentation shall register the page in an appropriate index.rst toctree. | event_driven | Prozess | nein | indirect |
| QR-0533-09 | When documentation is built, Qrisp documentation shall produce no new Sphinx warnings. | event_driven | Qualität (nicht funktional) | nein | indirect |
| QR-0533-10 | If a test fails before changes are made, then Qrisp contributors shall open a GitHub issue. | unwanted_behaviour | Prozess | nein | direct |
| QR-0533-11 | Before opening a pull request, Qrisp contributors shall run the test suite for the modified subsystem. | event_driven | Prozess | nein | direct |

#### PR 534

[github.com/eclipse-qrisp/Qrisp/pull/534](https://github.com/eclipse-qrisp/Qrisp/pull/534) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0534-01 | When converting an MLIR string to xDSL, MLIR_str_to_xdsl shall return a (ctx, module) tuple. | event_driven | Schnittstelle | nein | indirect |
| QR-0534-02 | When converting a JAXPR to xDSL, jaxpr_to_xdsl shall return a (ctx, module) tuple. | event_driven | Schnittstelle | nein | indirect |
| QR-0534-03 | When StableHLO lowering is enabled, FoldScalarLinalgGeneric shall fold 0-dimensional linalg.generic operations into scalar arithmetic. | event_driven | funktional/Leistung | nein | indirect |
| QR-0534-04 | When a 0-D tensor.extract(tensor.from_elements(x)) round-trip is encountered, FoldExtractFromElements shall replace the round-trip with x. | event_driven | funktional/Leistung | nein | indirect |
| QR-0534-05 | When a tensor.from_elements operation has no uses, EraseDeadFromElements shall erase the operation. | event_driven | funktional/Leistung | nein | indirect |
| QR-0534-06 | When comparing a zero-extended boolean against a constant 0 or 1, FoldCmpiExtui shall fold the comparison to an equivalent i1 expression. | event_driven | funktional/Leistung | nein | indirect |

#### PR 536

[github.com/eclipse-qrisp/Qrisp/pull/536](https://github.com/eclipse-qrisp/Qrisp/pull/536) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0536-01 | When IQAE runs in static mode, IQAE shall pass an int value for shots to get_measurement. | event_driven | Schnittstelle | nein | indirect |

#### PR 537

[github.com/eclipse-qrisp/Qrisp/pull/537](https://github.com/eclipse-qrisp/Qrisp/pull/537) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0537-01 | The carry_venting_adder shall update target to (target + d + c_in) modulo 2^n. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0537-02 | When terminal sampling an in-place addition with a quantum target containing fewer than six qubits, the venting adder shall produce deterministic results. | event_driven | funktional/Leistung | nein | indirect |
| QR-0537-03 | Qrisp shall list gidney_cq_venting_adder among its in-place adders. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 539

[github.com/eclipse-qrisp/Qrisp/pull/539](https://github.com/eclipse-qrisp/Qrisp/pull/539) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0539-01 | When lowering a stablehlo.case operation with two branches, stablehlo.case lowering shall treat a case indicator of zero as the true condition. | event_driven | funktional/Leistung | nein | indirect |

#### PR 541

[github.com/eclipse-qrisp/Qrisp/pull/541](https://github.com/eclipse-qrisp/Qrisp/pull/541) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0541-01 | While processing a composite gate with abstract parameters, Operation.inverse shall preserve the original gate's parameter list in the inverse gate. | state_driven | funktional/Leistung | nein | indirect |
| QR-0541-02 | While processing a composite gate with abstract parameters, Operation.inverse shall preserve the original gate's abstract-parameter set in the inverse gate. | state_driven | funktional/Leistung | nein | indirect |

#### PR 542

[github.com/eclipse-qrisp/Qrisp/pull/542](https://github.com/eclipse-qrisp/Qrisp/pull/542) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0542-01 | The maxCut reference documentation shall include create_maxcut_sample_array_post_processor. | ubiquitous | Prozess | nein | indirect |
| QR-0542-02 | The documentation for create_maxcut_sample_array_post_processor shall state that the function is intended for dynamic (Jasp) QAOA. | ubiquitous | Prozess | nein | indirect |
| QR-0542-03 | When invoked with a graph, create_maxcut_sample_array_post_processor shall return a JAX-traceable function that maps an array of integer-encoded bitstrings to a mean cut value as a zero-dimensional JAX array of float. | event_driven | Schnittstelle | nein | indirect |
| QR-0542-04 | While tracing mode is inactive, if the quantum variable length differs from the graph size, then maxcut_cost_operator shall raise a ValueError. | complex | funktional/Leistung | nein | indirect |

#### PR 543

[github.com/eclipse-qrisp/Qrisp/pull/543](https://github.com/eclipse-qrisp/Qrisp/pull/543) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0543-01 | The qrisp.typing module shall expose QubitLike for Qubit objects, integer indices, and sequences of either as qubit specifiers. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0543-02 | The qrisp.typing module shall expose ClbitLike for Clbit objects, integer indices, and sequences of either as classical-bit specifiers. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0543-03 | The qrisp.typing module shall expose ScalarLike for Python built-in scalars, NumPy scalar types, and JAX tracers. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0543-04 | The qrisp.typing module shall expose NDArrayLike for NumPy arrays, JAX arrays, and JAX tracers. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0543-05 | The qrisp.typing module shall expose ArrayLike as the union of ScalarLike and NDArrayLike. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0543-06 | The qrisp.typing module shall expose Param for Python numeric scalars, NumPy numeric scalars, symbolic expressions, concrete JAX arrays, and JAX tracers. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 544

[github.com/eclipse-qrisp/Qrisp/pull/544](https://github.com/eclipse-qrisp/Qrisp/pull/544) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0544-01 | When fredkin_qc receives num_ctrl_qubits, fredkin_qc shall create a Fredkin gate controlled by num_ctrl_qubits qubits. | event_driven | funktional/Leistung | nein | indirect |

#### PR 545

[github.com/eclipse-qrisp/Qrisp/pull/545](https://github.com/eclipse-qrisp/Qrisp/pull/545) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0545-01 | When used as a decorator of an existing in-place adder, Adder shall verify that the adder maps (a, b) to (a, a+b). | event_driven | funktional/Leistung | nein | indirect |

#### PR 551

[github.com/eclipse-qrisp/Qrisp/pull/551](https://github.com/eclipse-qrisp/Qrisp/pull/551) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0551-01 | When compiling a controlled U3Gate with a non-zero global phase, multi_controlled_u3_circ shall produce a definition circuit whose unitary matches the controlled operation's unitary. | event_driven | funktional/Leistung | nein | indirect |

#### PR 552

[github.com/eclipse-qrisp/Qrisp/pull/552](https://github.com/eclipse-qrisp/Qrisp/pull/552) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0552-01 | While processing a tutorial page with configured authorship data, tutorial_authors shall display the authorship information below the page title. | state_driven | funktional/Leistung | nein | direct |
| QR-0552-02 | If a tutorial page has no title, then tutorial_authors shall display the authorship information at the top of the page. | unwanted_behaviour | funktional/Leistung | nein | indirect |

#### PR 553

[github.com/eclipse-qrisp/Qrisp/pull/553](https://github.com/eclipse-qrisp/Qrisp/pull/553) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0553-01 | Qrisp shall require Python version 3.11 or later. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0553-02 | Qrisp shall define a dev dependency group that includes the ci and docs dependency groups. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0553-03 | Qrisp shall define a ci dependency group that includes the test, quantum-backends, chemistry, qec, and compiler dependency groups. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0553-04 | When installing dependencies, Qrisp shall install the editable project with the ci dependency group. | event_driven | Prozess | nein | indirect |

#### PR 556

[github.com/eclipse-qrisp/Qrisp/pull/556](https://github.com/eclipse-qrisp/Qrisp/pull/556) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0556-01 | The README.md shall list the IQM email address with the iqm.tech domain. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0556-02 | The author_email setting shall use the iqm.tech domain. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 561

[github.com/eclipse-qrisp/Qrisp/pull/561](https://github.com/eclipse-qrisp/Qrisp/pull/561) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0561-01 | README.md shall use the iqm.tech domain for IQM contact email addresses. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0561-02 | setup.cfg shall specify the Qrisp author email address in the iqm.tech domain. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 562

[github.com/eclipse-qrisp/Qrisp/pull/562](https://github.com/eclipse-qrisp/Qrisp/pull/562) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0562-01 | Qrisp shall include a Feedback and Contact section in its README. | ubiquitous | Prozess | nein | indirect |
| QR-0562-02 | Qrisp shall link to its Eclipse project page for author information in the README. | ubiquitous | Prozess | nein | indirect |

#### PR 564

[github.com/eclipse-qrisp/Qrisp/pull/564](https://github.com/eclipse-qrisp/Qrisp/pull/564) · 18 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0564-01 | The CircuitPass shall validate at runtime the QuantumCircuit-to-QuantumCircuit type contract of wrapped transformation functions. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0564-02 | When run() is called, the PassManager shall apply its CircuitPass instances in collection order. | event_driven | Schnittstelle | nein | indirect |
| QR-0564-03 | The arange_swaps pass shall reorder SWAP qubits to improve cancellation opportunities. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0564-04 | The cancel_inverses pass shall cancel adjacent gate-inverse pairs. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0564-05 | While processing gates controlled on \|0⟩, the cancel_zero_controls pass shall remove the gates. | state_driven | funktional/Leistung | nein | indirect |
| QR-0564-06 | The combine_single_qubit_gates pass shall fuse consecutive single-qubit gates. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0564-07 | The commute_swaps pass shall commute single-qubit operations past SWAP gates. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0564-08 | The convert_to_cz pass shall convert CX gates to CZ-based decompositions. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0564-09 | The convert_to_cz pass shall convert CY gates to CZ-based decompositions. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0564-10 | The convert_to_cz pass shall convert SWAP gates to CZ-based decompositions. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0564-11 | The decompose pass shall recursively dissolve synthesized gates. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0564-12 | The gray_synth_toffoli pass shall decompose Toffoli gates using Gray synthesis. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0564-13 | The is_toffoli predicate shall identify Toffoli gates. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0564-14 | The manual_layout pass shall re-index qubits according to a user-supplied mapping. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0564-15 | The remove_barriers pass shall remove barrier instructions. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0564-16 | The resolve_swaps pass shall fold SWAP gates into qubit-index remapping. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0564-17 | The reverse_parallelize pass shall perform reverse-order parallelization. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0564-18 | The visualize pass shall print the circuit without transforming it. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 568

[github.com/eclipse-qrisp/Qrisp/pull/568](https://github.com/eclipse-qrisp/Qrisp/pull/568) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0568-01 | jaspr_to_qir shall return QIR code for a given jaspr. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 571

[github.com/eclipse-qrisp/Qrisp/pull/571](https://github.com/eclipse-qrisp/Qrisp/pull/571) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0571-01 | Qrisp documentation shall omit the link to the Eclipse mailing list. | ubiquitous | Prozess | nein | indirect |

#### PR 572

[github.com/eclipse-qrisp/Qrisp/pull/572](https://github.com/eclipse-qrisp/Qrisp/pull/572) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0572-01 | While executing under Jasp, dicke_state shall prepare an equal superposition of states with the specified Hamming weight. | state_driven | funktional/Leistung | nein | indirect |
| QR-0572-02 | unbalanced_w_state shall prepare a generalized W state of Hamming weight 1 whose amplitudes are the normalized supplied amplitudes. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0572-03 | While executing under Jasp, unbalanced_w_state shall prepare a generalized W state from the supplied amplitudes. | state_driven | funktional/Leistung | nein | indirect |
| QR-0572-04 | While executing outside tracing mode, when the amplitude length differs from the quantum variable size, unbalanced_w_state shall raise ValueError. | complex | Schnittstelle | nein | indirect |
| QR-0572-05 | While executing outside tracing mode, when the amplitude vector is zero, unbalanced_w_state shall raise ValueError. | complex | Schnittstelle | nein | indirect |

#### PR 574

[github.com/eclipse-qrisp/Qrisp/pull/574](https://github.com/eclipse-qrisp/Qrisp/pull/574) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0574-01 | When `_to_pauli_dict` is invoked, QubitOperator shall return a dictionary representing the operator's Pauli expansion. | event_driven | Schnittstelle | nein | indirect |
| QR-0574-02 | When `_to_pauli_dict` is invoked, QubitOperator shall encode Pauli-string dictionary keys as tuples of `(index, pauli)` pairs sorted by qubit index. | event_driven | Schnittstelle | nein | indirect |
| QR-0574-03 | When `_to_pauli_dict` is invoked, QubitOperator shall represent the identity term with an empty tuple key. | event_driven | Schnittstelle | nein | indirect |
| QR-0574-04 | When `_to_pauli_dict` is invoked, QubitOperator shall associate a Pauli-string dictionary key with its scalar coefficient. | event_driven | Schnittstelle | nein | indirect |
| QR-0574-05 | QubitOperator shall designate its Pauli-dictionary conversion method for internal use. | ubiquitous | Schnittstelle | nein | direct |

#### PR 575

[github.com/eclipse-qrisp/Qrisp/pull/575](https://github.com/eclipse-qrisp/Qrisp/pull/575) · 7 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0575-01 | Jaspr.to_mlir shall accept a lower_stablehlo option that lowers StableHLO arithmetic and data operations to linalg, arith, and tensor dialects. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0575-02 | MLIR_str_to_xdsl shall return the xDSL Context and parsed module as a tuple. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0575-03 | jaxpr_to_xdsl shall return the xDSL Context and lowered xDSL module as a tuple. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0575-04 | When lower_stablehlo is enabled, jaspr_to_mlir shall replace a zero-dimensional single-output linalg.generic operation with equivalent scalar operations. | event_driven | funktional/Leistung | nein | indirect |
| QR-0575-05 | When a zero-dimensional tensor.extract consumes a single-element tensor.from_elements result, scalar_tensor_folding shall replace the extraction result with the underlying scalar. | event_driven | funktional/Leistung | nein | indirect |
| QR-0575-06 | When a tensor.from_elements result has no uses, EraseDeadFromElements shall erase the tensor.from_elements operation. | event_driven | funktional/Leistung | nein | indirect |
| QR-0575-07 | When a comparison evaluates a zero-extended i1 value against constant 0 or 1, FoldCmpiExtui shall replace the comparison with an equivalent i1 result. | event_driven | funktional/Leistung | nein | indirect |

#### PR 576

[github.com/eclipse-qrisp/Qrisp/pull/576](https://github.com/eclipse-qrisp/Qrisp/pull/576) · 8 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0576-01 | Where lower_stablehlo is true, Jaspr.to_mlir shall lower StableHLO arithmetic and data operations to linalg, arith, and tensor dialects. | optional_feature | Schnittstelle | nein | indirect |
| QR-0576-02 | Where lower_stablehlo is true, Jaspr.to_mlir shall rewrite StableHLO control flow involving quantum types to SCF. | optional_feature | funktional/Leistung | nein | indirect |
| QR-0576-03 | MLIR_str_to_xdsl shall return an xDSL Context and the parsed module as a tuple. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0576-04 | jaxpr_to_xdsl shall return an xDSL Context and the lowered module as a tuple. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0576-05 | When a linalg.generic operation has zero iterator types and one output tensor, FoldScalarLinalgGeneric shall replace it with equivalent scalar arithmetic. | event_driven | funktional/Leistung | nein | indirect |
| QR-0576-06 | When tensor.extract reads a zero-dimensional tensor.from_elements operation with one element, FoldExtractFromElements shall replace the extraction result with the original scalar. | event_driven | funktional/Leistung | nein | indirect |
| QR-0576-07 | When an arith.cmpi operation compares a zero-extended i1 value against constant 0 or 1, FoldCmpiExtui shall replace the comparison with an equivalent i1 expression. | event_driven | funktional/Leistung | nein | indirect |
| QR-0576-08 | When constructing a multi-controlled U3 operation, multi_controlled_u3_circ shall account for the U3 gate global phase. | event_driven | funktional/Leistung | nein | indirect |

#### PR 577

[github.com/eclipse-qrisp/Qrisp/pull/577](https://github.com/eclipse-qrisp/Qrisp/pull/577) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0577-01 | The MLIR_str_to_xdsl function shall return the xDSL Context together with the parsed xDSL module. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0577-02 | The jaxpr_to_xdsl function shall return the xDSL Context together with the xDSL module containing the lowered program. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0577-03 | Where StableHLO lowering is enabled, scalar_linalg_folding shall fold a zero-dimensional single-output linalg.generic operation into scalar arithmetic. | optional_feature | funktional/Leistung | nein | indirect |
| QR-0577-04 | When a tensor.extract operation reads a zero-dimensional tensor.from_elements result, scalar_tensor_folding shall replace the extract result with the underlying scalar. | event_driven | funktional/Leistung | nein | indirect |
| QR-0577-05 | If a tensor.from_elements operation has no active uses, then EraseDeadFromElements shall erase the operation. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0577-06 | When an arith.cmpi comparison has a zero-extended i1 operand and a constant right-hand value in {0, 1}, FoldCmpiExtui shall replace it with the equivalent i1 result. | event_driven | funktional/Leistung | nein | indirect |

#### PR 579

[github.com/eclipse-qrisp/Qrisp/pull/579](https://github.com/eclipse-qrisp/Qrisp/pull/579) · 8 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0579-01 | When given target polynomial coefficients, gqsp_angles shall return GQSP angles and a scaling factor that reconstruct the target polynomial. | event_driven | funktional/Leistung | nein | indirect |
| QR-0579-02 | When given target polynomial coefficients, poly_to_nlft_sequence shall return a non-linear Fourier sequence and scaling factor whose response matches the target polynomial magnitude on the unit circle. | event_driven | funktional/Leistung | nein | indirect |
| QR-0579-03 | qsp_angles shall accept even and odd parity settings. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0579-04 | qsp_angles shall accept X and Z signal-basis settings. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0579-05 | When given target polynomial coefficients with a specified parity, qsp_angles shall return QSP phase angles and a scaling factor that reconstruct the target polynomial. | event_driven | funktional/Leistung | nein | indirect |
| QR-0579-06 | When given target polynomial coefficients with a specified parity, qsvt_angles shall return QSVT phase angles and a scaling factor that reconstruct the target polynomial. | event_driven | funktional/Leistung | nein | indirect |
| QR-0579-07 | When called, xqsp_angles shall raise NotImplementedError. | event_driven | Schnittstelle | nein | indirect |
| QR-0579-08 | When called, yqsp_angles shall raise NotImplementedError. | event_driven | Schnittstelle | nein | indirect |

#### PR 582

[github.com/eclipse-qrisp/Qrisp/pull/582](https://github.com/eclipse-qrisp/Qrisp/pull/582) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0582-01 | When `unitary()` runs in JASP/dynamic mode after its U3 angles become JAX values, `unitary()` shall trace the unitary application. | event_driven | funktional/Leistung | nein | indirect |

#### PR 585

[github.com/eclipse-qrisp/Qrisp/pull/585](https://github.com/eclipse-qrisp/Qrisp/pull/585) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0585-01 | While Jasp tracing is active, the barrier function shall act as a no-op. | state_driven | funktional/Leistung | nein | indirect |
| QR-0585-02 | While Jasp tracing is inactive, the barrier function shall apply a circuit barrier to the supplied qubits. | state_driven | funktional/Leistung | nein | indirect |

#### PR 587

[github.com/eclipse-qrisp/Qrisp/pull/587](https://github.com/eclipse-qrisp/Qrisp/pull/587) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0587-01 | When exact is True and winner_state_amount is not specified, grovers_alg shall raise a ValueError. | complex | Schnittstelle | nein | indirect |
| QR-0587-02 | grovers_alg shall accept a Sequence of QuantumVariable or QuantumArray objects as args. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0587-03 | When iterations is not specified, grovers_alg shall calculate the optimal iteration count from winner_state_amount. | event_driven | funktional/Leistung | nein | indirect |
| QR-0587-04 | When an oracle acts on QuantumVariables outside args, grovers_alg shall execute the oracle without raising an oracle-uncompute exception. | event_driven | funktional/Leistung | nein | indirect |
| QR-0587-05 | When an oracle_function uses auxiliary QuantumVariables, oracle_function shall uncompute the auxiliary QuantumVariables. | event_driven | Schnittstelle | nein | direct |
| QR-0587-06 | When an oracle tags a number of states equal to the search-space size, grovers_alg shall produce equal measurement probabilities for the tagged states. | event_driven | funktional/Leistung | nein | indirect |

#### PR 588

[github.com/eclipse-qrisp/Qrisp/pull/588](https://github.com/eclipse-qrisp/Qrisp/pull/588) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0588-01 | When args is a QuantumArray, amplitude_amplification shall accept the QuantumArray as a direct input. | event_driven | Schnittstelle | nein | indirect |
| QR-0588-02 | When kwargs_oracle is omitted, amplitude_amplification shall initialize oracle keyword arguments with an empty dictionary. | event_driven | Schnittstelle | nein | indirect |
| QR-0588-03 | When reflection_indices is specified, amplitude_amplification shall perform the reflection with respect to the indicated flattened arguments. | event_driven | funktional/Leistung | nein | indirect |

#### PR 589

[github.com/eclipse-qrisp/Qrisp/pull/589](https://github.com/eclipse-qrisp/Qrisp/pull/589) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0589-01 | When `args` is a QuantumVariable or QuantumArray, QAE shall accept the object as the `args` argument. | event_driven | Schnittstelle | nein | indirect |
| QR-0589-02 | When `args` is a sequence, QAE shall pass its elements as separate positional arguments to state_function. | event_driven | Schnittstelle | nein | indirect |
| QR-0589-03 | When `args` is a sequence, QAE shall pass its elements as separate positional arguments to oracle_function. | event_driven | Schnittstelle | nein | indirect |
| QR-0589-04 | If neither `precision` nor `target` is provided, then QAE shall raise a ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |

#### PR 591

[github.com/eclipse-qrisp/Qrisp/pull/591](https://github.com/eclipse-qrisp/Qrisp/pull/591) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0591-01 | While Jasp dynamically traces quantum operands with unequal register sizes, ammend_inpl_adder shall add the source operand to the target operand modulo the target width. | state_driven | funktional/Leistung | nein | indirect |
| QR-0591-02 | While Jasp dynamically traces a classical source input, ammend_inpl_adder shall add the source value to the quantum target modulo the target width. | state_driven | funktional/Leistung | nein | indirect |
| QR-0591-03 | When qq_gidney_adder performs controlled addition with a one-qubit target register, qq_gidney_adder shall add the source operand modulo two when the control is enabled. | event_driven | funktional/Leistung | nein | indirect |
| QR-0591-04 | When the test_jasp parameter is true, inpl_adder_test shall run quantum-quantum correctness checks through boolean_simulation in dynamic Jasp mode. | event_driven | funktional/Leistung | nein | indirect |
| QR-0591-05 | When the test_jasp parameter is true, inpl_adder_test shall run classical-quantum correctness checks through boolean_simulation in dynamic Jasp mode. | event_driven | funktional/Leistung | nein | indirect |

#### PR 593

[github.com/eclipse-qrisp/Qrisp/pull/593](https://github.com/eclipse-qrisp/Qrisp/pull/593) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0593-01 | decompose_composite_gates shall return a new Jaspr containing only primitive quantum gates. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0593-02 | Where a Jaspr contains a sub-jaxpr nested in jit, while, cond, or scan, decompose_composite_gates shall recursively decompose composite gates in the nested sub-jaxpr. | optional_feature | funktional/Leistung | nein | indirect |
| QR-0593-03 | When multiple jit equations reference the same ClosedJaxpr object, the decomposed jaspr shall retain the same transformed ClosedJaxpr object for those equations. | event_driven | Qualität (nicht funktional) | nein | indirect |
| QR-0593-04 | When a Jaspr containing composite gates is passed to decompose_composite_gates, decompose_composite_gates shall preserve the Jaspr's output probability distribution. | event_driven | funktional/Leistung | nein | indirect |

#### PR 595

[github.com/eclipse-qrisp/Qrisp/pull/595](https://github.com/eclipse-qrisp/Qrisp/pull/595) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0595-01 | When executed, the q_fori_loop documentation example shall complete without raising a NameError that reports k as undefined. | event_driven | Qualität (nicht funktional) | nein | indirect |

#### PR 597

[github.com/eclipse-qrisp/Qrisp/pull/597](https://github.com/eclipse-qrisp/Qrisp/pull/597) · 7 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0597-01 | When a caller supplies custom PREP and UNPREP subroutines, BlockEncoding.from_foqcs_lcu_prep shall construct a FOQCS-LCU block encoding. | event_driven | Schnittstelle | nein | indirect |
| QR-0597-02 | When a caller supplies an operator input, BlockEncoding.from_foqcs_lcu_operator shall construct a FOQCS-LCU block encoding. | event_driven | Schnittstelle | nein | indirect |
| QR-0597-03 | When applying a FOQCS-LCU block encoding, BlockEncoding.apply shall produce the statevector from the encoding definition. | event_driven | funktional/Leistung | nein | indirect |
| QR-0597-04 | When applied under the jasp environment, BlockEncoding.apply_rus shall produce the same statevector as BlockEncoding.apply. | event_driven | funktional/Leistung | nein | indirect |
| QR-0597-05 | If a caller supplies an invalid ancillary-qubit count, then BlockEncoding.from_foqcs_lcu_prep shall reject the input. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0597-06 | The from_foqcs_lcu_prep documentation shall state that the method is designed for building custom FOQCS-LCU block encodings. | ubiquitous | Prozess | nein | direct |
| QR-0597-07 | The tests shall include a docstring explaining what the test does. | ubiquitous | Prozess | nein | direct |

#### PR 599

[github.com/eclipse-qrisp/Qrisp/pull/599](https://github.com/eclipse-qrisp/Qrisp/pull/599) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0599-01 | When jaspr_to_mlir lowers a Jaspr to MLIR, jaspr_to_mlir shall recursively expand composite gates before JAXPR-to-xDSL lowering. | event_driven | funktional/Leistung | nein | indirect |

#### PR 601

[github.com/eclipse-qrisp/Qrisp/pull/601](https://github.com/eclipse-qrisp/Qrisp/pull/601) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0601-01 | When _apply_op inlines a composite gate with parameter tracers, _apply_op shall bind each parameterized primitive sub-gate with a tracer for each of its abstract parameters. | event_driven | funktional/Leistung | nein | direct |
| QR-0601-02 | When quantum_gate_lowering lowers a gate parameter that is a symbolic expression of a runtime operand, quantum_gate_lowering shall emit an MLIR operand that evaluates the symbolic expression. | event_driven | Schnittstelle | nein | direct |
| QR-0601-03 | _decompose_sub_jaxpr shall propagate composite-gate decomposition into nested JAX sub-jaxprs. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 602

[github.com/eclipse-qrisp/Qrisp/pull/602](https://github.com/eclipse-qrisp/Qrisp/pull/602) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0602-01 | When decompose_composite_gates decomposes a primitive sub-gate with symbolic parameters, decompose_composite_gates shall emit the evaluated parameter values as dynamic invars in the resulting JASPR. | event_driven | Schnittstelle | nein | indirect |
| QR-0602-02 | When decompose_composite_gates decomposes a primitive sub-gate with constant parameters, decompose_composite_gates shall emit the parameter values as explicit input variables in the resulting JASPR. | event_driven | Schnittstelle | nein | indirect |
| QR-0602-03 | When decompose_composite_gates decomposes a parametrized composite gate, decompose_composite_gates shall produce a JASPR with the same unitary as the original JASPR. | event_driven | funktional/Leistung | nein | indirect |

#### PR 604

[github.com/eclipse-qrisp/Qrisp/pull/604](https://github.com/eclipse-qrisp/Qrisp/pull/604) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0604-01 | When a `@qache`d quantum function that closes over a constant JAX array is called inside a control block, the control transformation shall preserve the closed-over constant JAX array when constructing the controlled function. | event_driven | funktional/Leistung | nein | direct |

#### PR 607

[github.com/eclipse-qrisp/Qrisp/pull/607](https://github.com/eclipse-qrisp/Qrisp/pull/607) · 7 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0607-01 | QSVT shall return a BlockEncoding representing a singular-value polynomial transformation of its input operator. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0607-02 | When parity is "odd", QSVT shall return a BlockEncoding of U p_odd(Σ) V† for an input operator A=UΣV†. | event_driven | funktional/Leistung | nein | indirect |
| QR-0607-03 | When parity is "even", QSVT shall return a BlockEncoding of V p_even(Σ) V† for an input operator A=UΣV†. | event_driven | funktional/Leistung | nein | indirect |
| QR-0607-04 | When dagger is invoked, BlockEncoding shall return a new BlockEncoding representing the Hermitian conjugate of the operator. | event_driven | Schnittstelle | nein | indirect |
| QR-0607-05 | inversion shall default its method argument to QSVT. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0607-06 | BlockEncoding shall provide a pseudo_inv method that returns a BlockEncoding approximating the threshold matrix pseudoinverse of the operator. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0607-07 | BlockEncoding shall provide an svt method that returns a BlockEncoding representing a singular value transformation of the operator. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 609

[github.com/eclipse-qrisp/Qrisp/pull/609](https://github.com/eclipse-qrisp/Qrisp/pull/609) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0609-01 | When concatenating a list with a DynamicQubitArray, DynamicQubitArray shall recognize a tracer item as an AbstractQubit when the item's abstract value is an AbstractQubit. | event_driven | Schnittstelle | nein | indirect |
| QR-0609-02 | When a list is added before a DynamicQubitArray, DynamicQubitArray shall place its existing qubits before the list qubits. | event_driven | funktional/Leistung | nein | indirect |

#### PR 610

[github.com/eclipse-qrisp/Qrisp/pull/610](https://github.com/eclipse-qrisp/Qrisp/pull/610) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0610-01 | When passed a Cirq Circuit, QuantumCircuit.from_cirq shall return the converted QuantumCircuit. | event_driven | Schnittstelle | nein | indirect |
| QR-0610-02 | When passed a Cirq circuit produced by convert_to_cirq, QuantumCircuit.from_cirq shall preserve the circuit statevector. | event_driven | funktional/Leistung | nein | indirect |
| QR-0610-03 | If Cirq is not installed, then convert_to_cirq shall raise an ImportError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0610-04 | If a gate cannot be decomposed into elementary instructions, then convert_to_cirq shall raise ValueError. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0610-05 | When converting a Qrisp circuit containing a global-phase operation, convert_to_cirq shall preserve the global phase in the Cirq circuit. | event_driven | funktional/Leistung | nein | indirect |

#### PR 612

[github.com/eclipse-qrisp/Qrisp/pull/612](https://github.com/eclipse-qrisp/Qrisp/pull/612) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0612-01 | When a QubitOperator multiplication operation produces a term whose coefficient magnitude is below QubitOperator's threshold, QubitOperator shall omit the term from its terms dictionary. | event_driven | funktional/Leistung | nein | direct |

#### PR 613

[github.com/eclipse-qrisp/Qrisp/pull/613](https://github.com/eclipse-qrisp/Qrisp/pull/613) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0613-01 | The qrisp.typing module shall export FloatLike as a gate-parameter type alias. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0613-02 | The FloatLike type alias shall include Python float and integer values, NumPy floating-point and integer scalars, SymPy expressions, JAX arrays, and JAX tracers as gate parameter values. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0613-03 | The FloatLike type alias shall exclude complex Python values and complex NumPy scalar values from gate parameter values. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 614

[github.com/eclipse-qrisp/Qrisp/pull/614](https://github.com/eclipse-qrisp/Qrisp/pull/614) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0614-01 | When exp_value_backend is provided for the exp_value objective, optimization_routine shall calculate the expectation value through measurement using exp_value_backend. | event_driven | Schnittstelle | nein | indirect |
| QR-0614-02 | If exp_value_backend is not provided, then optimization_routine shall attempt expectation-value calculation with statevector simulation. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0614-03 | Where exp_value_backend is not provided, if statevector calculation raises MemoryError, ValueError, or RuntimeError, then optimization_routine shall calculate the expectation value using measurement. | complex | funktional/Leistung | nein | indirect |
| QR-0614-04 | run shall use 0.01 as the default precision for expectation-value calculations. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 615

[github.com/eclipse-qrisp/Qrisp/pull/615](https://github.com/eclipse-qrisp/Qrisp/pull/615) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0615-01 | When c_in is supplied in the \|1> state, cuccaro_adder shall add the carry-in value to b. | event_driven | funktional/Leistung | nein | indirect |
| QR-0615-02 | If c_in is supplied as a value other than QuantumBool or Qubit in static mode, then cuccaro_adder shall raise a TypeError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0615-03 | If c_out is supplied as a value other than QuantumBool or Qubit in static mode, then cuccaro_adder shall raise a TypeError. | unwanted_behaviour | Schnittstelle | nein | indirect |

#### PR 618

[github.com/eclipse-qrisp/Qrisp/pull/618](https://github.com/eclipse-qrisp/Qrisp/pull/618) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0618-01 | When invoked during Jasp tracing, thapliyal_adder shall complete tracing without a TracerIntegerConversionError. | event_driven | funktional/Leistung | nein | direct |
| QR-0618-02 | When both input registers have size 1, thapliyal_adder shall apply a CNOT from the first input register to the second input register. | event_driven | funktional/Leistung | nein | direct |
| QR-0618-03 | When the input registers have unequal sizes, thapliyal_adder shall preserve the second input register size. | event_driven | funktional/Leistung | nein | direct |
| QR-0618-04 | When called inside a control block in static mode, thapliyal_adder shall perform controlled addition. | event_driven | funktional/Leistung | nein | direct |
| QR-0618-05 | When called inside a control block in dynamic mode, thapliyal_adder shall perform controlled addition. | event_driven | funktional/Leistung | nein | direct |
| QR-0618-06 | When its first argument is an int, thapliyal_adder shall convert the argument to a quantum register automatically. | event_driven | Schnittstelle | nein | direct |

#### PR 619

[github.com/eclipse-qrisp/Qrisp/pull/619](https://github.com/eclipse-qrisp/Qrisp/pull/619) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0619-01 | The Job base class shall define result, cancel, and status as its three abstract methods. | ubiquitous | Schnittstelle | nein | direct |
| QR-0619-02 | When Backend.run_async returns a Job, the Backend shall return the Job after execution has been handed off to the backend. | event_driven | Schnittstelle | nein | direct |
| QR-0619-03 | When a Job object is constructed, the Job shall initialize its status to INITIALIZING. | event_driven | funktional/Leistung | nein | direct |

#### PR 621

[github.com/eclipse-qrisp/Qrisp/pull/621](https://github.com/eclipse-qrisp/Qrisp/pull/621) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0621-01 | When a list of qubits is reverse-concatenated with a DynamicQubitArray, DynamicQubitArray shall prepend the list elements in their original order. | event_driven | Schnittstelle | nein | direct |

#### PR 622

[github.com/eclipse-qrisp/Qrisp/pull/622](https://github.com/eclipse-qrisp/Qrisp/pull/622) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0622-01 | QrispSimulatorBackend shall accept a PassManager or None through the pm keyword argument. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0622-02 | If pm is neither a PassManager nor None, then QrispSimulatorBackend shall raise TypeError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0622-03 | While a PassManager is provided at construction, QrispSimulatorBackend shall apply it to each circuit before simulation. | state_driven | funktional/Leistung | nein | indirect |
| QR-0622-04 | While pm contains no passes, QrispSimulatorBackend shall preserve the simulation result of each circuit. | state_driven | funktional/Leistung | nein | direct |
| QR-0622-05 | While pm contains multiple passes, QrispSimulatorBackend shall apply the passes in their configured order before simulation. | state_driven | funktional/Leistung | nein | direct |

#### PR 623

[github.com/eclipse-qrisp/Qrisp/pull/623](https://github.com/eclipse-qrisp/Qrisp/pull/623) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0623-01 | Qrisp shall export fuse_adjacents from its top-level namespace. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0623-02 | The fuse_adjacents circuit pass shall fuse adjacent gate pairs. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0623-03 | The fuse_adjacents circuit pass shall preserve the unitary of transformed circuits. | ubiquitous | funktional/Leistung | nein | direct |
| QR-0623-04 | The fuse_adjacents circuit pass shall preserve measurement statistics of transformed circuits. | ubiquitous | funktional/Leistung | nein | direct |

#### PR 624

[github.com/eclipse-qrisp/Qrisp/pull/624](https://github.com/eclipse-qrisp/Qrisp/pull/624) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0624-01 | When building HTML documentation, Qrisp shall emit zero DeprecationWarnings from Qrisp source. | event_driven | Qualität (nicht funktional) | nein | indirect |
| QR-0624-02 | When building HTML documentation, Qrisp documentation shall emit zero Sphinx warnings for duplicate object descriptions, title underlines, documents absent from a toctree. | event_driven | Qualität (nicht funktional) | nein | indirect |

#### PR 625

[github.com/eclipse-qrisp/Qrisp/pull/625](https://github.com/eclipse-qrisp/Qrisp/pull/625) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0625-01 | The Qiskit circuit converter shall emit no DeprecationWarning from CircuitInstruction access. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 627

[github.com/eclipse-qrisp/Qrisp/pull/627](https://github.com/eclipse-qrisp/Qrisp/pull/627) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0627-01 | The reflection function shall expose qargs with the type annotation QuantumVariable \| QuantumArray \| Sequence[QuantumVariable \| QuantumArray]. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0627-02 | When the args parameter is None, the reflection function shall use an empty sequence as the additional state-function arguments. | event_driven | Schnittstelle | nein | indirect |
| QR-0627-03 | When the kwargs parameter is None, the reflection function shall use an empty dictionary as the state-function keyword arguments. | event_driven | Schnittstelle | nein | indirect |

#### PR 628

[github.com/eclipse-qrisp/Qrisp/pull/628](https://github.com/eclipse-qrisp/Qrisp/pull/628) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0628-01 | When a client imports BlockEncoding from qrisp.block_encodings, Qrisp shall provide the BlockEncoding class. | event_driven | Schnittstelle | nein | indirect |
| QR-0628-02 | When a caller provides an array that is not a two-dimensional square matrix, BlockEncoding.from_array shall raise ValueError. | event_driven | Schnittstelle | nein | indirect |
| QR-0628-03 | When a caller provides an array whose dimension is not a positive power of two, BlockEncoding.from_array shall raise ValueError. | event_driven | Schnittstelle | nein | indirect |
| QR-0628-04 | When a caller provides negative coefficients, BlockEncoding.from_lcu shall raise ValueError. | event_driven | Schnittstelle | nein | indirect |

#### PR 634

[github.com/eclipse-qrisp/Qrisp/pull/634](https://github.com/eclipse-qrisp/Qrisp/pull/634) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0634-01 | The documentation build shall process Markdown and Jupyter Notebook files as documentation sources. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0634-02 | During documentation builds, the documentation build shall limit notebook execution to 60 seconds. | state_driven | funktional/Leistung | nein | indirect |
| QR-0634-03 | During documentation builds, when notebook execution fails, the documentation build shall print the full traceback to standard error. | complex | funktional/Leistung | nein | indirect |
| QR-0634-04 | During documentation builds, the documentation build shall exclude BigInteger.ipynb, FT_compilation.ipynb, Jasp.ipynb, and QIROtutorial.ipynb from execution. | state_driven | funktional/Leistung | nein | indirect |
| QR-0634-05 | When myst-nb interprets an intra-notebook heading anchor link as a cross-reference, the documentation build shall suppress the myst.xref_missing warning. | event_driven | funktional/Leistung | nein | indirect |

#### PR 636

[github.com/eclipse-qrisp/Qrisp/pull/636](https://github.com/eclipse-qrisp/Qrisp/pull/636) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0636-01 | When adding a future global mechanical change, the .git-blame-ignore-revs file shall list the full SHA of its commit. | event_driven | Prozess | nein | insufficient |

#### PR 637

[github.com/eclipse-qrisp/Qrisp/pull/637](https://github.com/eclipse-qrisp/Qrisp/pull/637) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0637-01 | When documenting assignment of a string to a QuantumString, the QuantumString documentation shall show construction with a size equal to the assigned string length. | event_driven | Prozess | nein | indirect |
| QR-0637-02 | When documenting assignment of [[1,0],[0,1]] to a QuantumArray, the QuantumArray documentation shall show construction with shape (2, 2). | event_driven | Prozess | nein | indirect |

#### PR 641

[github.com/eclipse-qrisp/Qrisp/pull/641](https://github.com/eclipse-qrisp/Qrisp/pull/641) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0641-01 | QuantumArrayIterator shall return itself from its __iter__ method. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 642

[github.com/eclipse-qrisp/Qrisp/pull/642](https://github.com/eclipse-qrisp/Qrisp/pull/642) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0642-01 | QuantumArray.reshape shall accept NumPy's order keyword. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0642-02 | When dot receives a one-dimensional QuantumArray and a two-dimensional QuantumArray, dot shall compute their product. | event_driven | funktional/Leistung | nein | indirect |
| QR-0642-03 | When iterated, QuantumArrayIterator shall return itself. | event_driven | Schnittstelle | nein | direct |

#### PR 643

[github.com/eclipse-qrisp/Qrisp/pull/643](https://github.com/eclipse-qrisp/Qrisp/pull/643) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0643-01 | When executed with Python 3.11, the GitHub Actions CI job shall complete dependency installation successfully. | event_driven | Prozess | nein | indirect |

#### PR 645

[github.com/eclipse-qrisp/Qrisp/pull/645](https://github.com/eclipse-qrisp/Qrisp/pull/645) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0645-01 | The checkout action configuration shall specify actions/checkout version v6. | ubiquitous | Prozess | nein | indirect |
| QR-0645-02 | The pytest test command shall target tests/circuit_tests/operation_tests/test_standard_operations.py::TestSXGate. | ubiquitous | Prozess | nein | indirect |

#### PR 646

[github.com/eclipse-qrisp/Qrisp/pull/646](https://github.com/eclipse-qrisp/Qrisp/pull/646) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0646-01 | The landing page example shall initialize the Qiskit Aer backend using the current API. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 647

[github.com/eclipse-qrisp/Qrisp/pull/647](https://github.com/eclipse-qrisp/Qrisp/pull/647) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0647-01 | BlockEncoding.from_lcu shall accept a one-dimensional array containing complex coefficients. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0647-02 | When coefficients are outside the real non-negative domain, BlockEncoding.from_lcu shall construct a BlockEncoding representing the supplied linear combination of unitaries. | event_driven | funktional/Leistung | nein | indirect |
| QR-0647-03 | BlockEncoding.from_lcu shall set the BlockEncoding normalization factor to the sum of coefficient magnitudes. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0647-04 | When a single unitary is provided with a coefficient whose imaginary-part magnitude is at least 1e-12, BlockEncoding.from_lcu shall raise ValueError. | event_driven | Schnittstelle | nein | indirect |

#### PR 650

[github.com/eclipse-qrisp/Qrisp/pull/650](https://github.com/eclipse-qrisp/Qrisp/pull/650) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0650-01 | QubitOperator shall omit the get_measurement method from its public interface. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0650-02 | FermionicOperator shall omit the get_measurement method from its public interface. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0650-03 | Hamiltonian shall omit the get_measurement abstract method. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 651

[github.com/eclipse-qrisp/Qrisp/pull/651](https://github.com/eclipse-qrisp/Qrisp/pull/651) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0651-01 | QubitOperator shall omit the pauli_block_encoding method. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0651-02 | The BlockEncoding module shall expose the BlockEncoding.from_operator constructor. | ubiquitous | Schnittstelle | nein | direct |

#### PR 652

[github.com/eclipse-qrisp/Qrisp/pull/652](https://github.com/eclipse-qrisp/Qrisp/pull/652) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0652-01 | When jrange receives three arguments, jrange shall emit a QrispDeprecationWarning stating that the step argument was removed. | event_driven | Schnittstelle | nein | indirect |
| QR-0652-02 | When jrange receives three arguments, jrange shall raise a TypeError indicating that it accepts one or two arguments. | event_driven | Schnittstelle | nein | indirect |

#### PR 653

[github.com/eclipse-qrisp/Qrisp/pull/653](https://github.com/eclipse-qrisp/Qrisp/pull/653) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0653-01 | When numpydoc reports UserWarnings for literal circuit output in docstring code blocks, the Qrisp documentation configuration shall suppress the warnings. | event_driven | Qualität (nicht funktional) | nein | indirect |
| QR-0653-02 | When Python parses Qrisp docstrings containing backslash escape sequences, Qrisp source code shall avoid deprecation warnings. | event_driven | Qualität (nicht funktional) | nein | indirect |

#### PR 654

[github.com/eclipse-qrisp/Qrisp/pull/654](https://github.com/eclipse-qrisp/Qrisp/pull/654) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0654-01 | When a user hovers over a tutorial card, the tutorials page shall display the card's tutorial description as a hover overlay. | event_driven | funktional/Leistung | nein | direct |

#### PR 658

[github.com/eclipse-qrisp/Qrisp/pull/658](https://github.com/eclipse-qrisp/Qrisp/pull/658) · 10 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0658-01 | When changelog-dev.rst is unmodified in a pull request, the Changelog Check workflow shall post or update a reminder comment. | event_driven | Prozess | nein | indirect |
| QR-0658-02 | When changelog-dev.rst is unmodified in a pull request, the Changelog Check workflow shall fail CI. | event_driven | Prozess | nein | indirect |
| QR-0658-03 | When changelog-dev.rst is modified in a pull request, the Changelog Check workflow shall post or update an acknowledgment comment. | event_driven | Prozess | nein | indirect |
| QR-0658-04 | When run after the release version is set in pyproject.toml, prepare-release-changelog.py shall archive changelog-dev.rst as <version>.rst. | event_driven | Prozess | nein | indirect |
| QR-0658-05 | prepare-release-changelog.py shall insert the release version into the index.rst toctree in descending order. | ubiquitous | Prozess | nein | indirect |
| QR-0658-06 | prepare-release-changelog.py shall create a fresh changelog-dev.rst for the next minor release. | ubiquitous | Prozess | nein | indirect |
| QR-0658-07 | The developer changelog entry shall explain what changed and why. | ubiquitous | Prozess | nein | direct |
| QR-0658-08 | The developer changelog entry shall reference its pull request using `PR #NNN <URL>`. | ubiquitous | Prozess | nein | direct |
| QR-0658-09 | The developer changelog entry shall identify the affected component. | ubiquitous | Prozess | nein | direct |
| QR-0658-10 | Where a deprecation applies, the developer changelog entry shall identify the replacement API. | optional_feature | Prozess | nein | direct |

#### PR 659

[github.com/eclipse-qrisp/Qrisp/pull/659](https://github.com/eclipse-qrisp/Qrisp/pull/659) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0659-01 | When a caller imports IQMBackend from qrisp.interface, qrisp.interface shall provide the IQMBackend implementation from iqm-client. | event_driven | Schnittstelle | nein | indirect |
| QR-0659-02 | If iqm-client with Qrisp support is unavailable when IQMBackend is requested, then qrisp.interface shall raise ImportError that instructs the caller to install qrisp[iqm]. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0659-03 | Where the iqm installation extra is selected, Qrisp shall include iqm-client as an installation dependency. | optional_feature | Schnittstelle | nein | indirect |

#### PR 660

[github.com/eclipse-qrisp/Qrisp/pull/660](https://github.com/eclipse-qrisp/Qrisp/pull/660) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0660-01 | The Qrisp test suite shall produce deterministic results for some stochastic tests. | ubiquitous | Prozess | nein | indirect |

#### PR 663

[github.com/eclipse-qrisp/Qrisp/pull/663](https://github.com/eclipse-qrisp/Qrisp/pull/663) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0663-01 | IQMBackend shall implement Qrisp's Backend interface for executing circuits on IQM hardware. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0663-02 | IQMJob shall return per-circuit measurement-count histograms for completed IQM jobs. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0663-03 | When cancel is called on an IQMJob outside a terminal state, IQMJob shall dispatch cancellation to its underlying IQM job. | event_driven | Schnittstelle | nein | indirect |
| QR-0663-04 | IQMJob shall expose the underlying IQM UUID through its job_id property. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0663-05 | When IQMJob.status is called, IQMJob shall translate IQM statuses waiting, processing, completed, failed, cancelled to Qrisp statuses QUEUED, RUNNING, DONE, ERROR, CANCELLED, respectively. | event_driven | Schnittstelle | nein | indirect |
| QR-0663-06 | When qrisp.interface is imported in an environment without qrisp[iqm], qrisp.interface shall load without raising ImportError. | event_driven | Schnittstelle | nein | indirect |

#### PR 664

[github.com/eclipse-qrisp/Qrisp/pull/664](https://github.com/eclipse-qrisp/Qrisp/pull/664) · 9 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0664-01 | Qrisp shall provide an aqt optional-dependency group that installs qiskit-aqt-provider version 1.15.0. | ubiquitous | Schnittstelle | nein | direct |
| QR-0664-02 | Qrisp shall provide a catalyst optional-dependency group. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0664-03 | Qrisp shall provide an xdsl optional-dependency group. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0664-04 | Qrisp shall provide a docs optional-dependency group. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0664-05 | Qrisp shall provide a test optional-dependency group. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0664-06 | Qrisp shall provide an iqm optional-dependency group. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0664-07 | Qrisp shall provide a qiskit optional-dependency group. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0664-08 | Qrisp shall require Python versions from 3.11 inclusive through 3.13 exclusive. | ubiquitous | Schnittstelle | nein | direct |
| QR-0664-09 | When the docs-install target runs, the documentation Makefile shall install Qrisp's docs extras from the repository root. | event_driven | Prozess | nein | direct |

#### PR 665

[github.com/eclipse-qrisp/Qrisp/pull/665](https://github.com/eclipse-qrisp/Qrisp/pull/665) · 25 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0665-01 | The BlockEncoding.svt method shall apply a polynomial to the singular values of a block-encoded operator. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0665-02 | When singular values are below a specified threshold, the BlockEncoding.pseudo_inv method shall ignore the values in its threshold pseudoinverse. | event_driven | Schnittstelle | nein | indirect |
| QR-0665-03 | The BlockEncoding.inv method shall use QSVT by default to invert block-encoded operators. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0665-04 | The BlockEncoding.dagger method shall return the adjoint of a block-encoded operator. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0665-05 | The BlockEncoding.from_eye method shall construct a block encoding of a two-dimensional array with ones on a specified diagonal and zeros elsewhere. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0665-06 | The BlockEncoding.from_projector method shall construct a block encoding of the projector \|φ⟩⟨ψ\|. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0665-07 | When kernel=True, the BlockEncoding.from_projector method shall construct a block encoding of the kernel projector. | event_driven | Schnittstelle | nein | indirect |
| QR-0665-08 | The BlockEncoding.from_foqcs_lcu_operator method shall construct a block encoding from a QubitOperator using the FOQCS-LCU algorithm. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0665-09 | The BlockEncoding.from_foqcs_lcu_prep method shall construct custom FOQCS-LCU block encodings from supplied right and left PREP subroutines. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0665-10 | The BlockEncoding.from_lcu method shall support general complex coefficients. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0665-11 | The QSVT function shall perform Quantum Singular Value Transform for fixed-parity real polynomials. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0665-12 | The GQSVT function shall perform Generalized Quantum Singular Value Transform for fixed-parity complex polynomials. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0665-13 | The dalzell_inversion function shall implement the Dalzell Quantum Linear System Solver using QSVT-based kernel reflection. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0665-14 | The Backend class shall return an immediate Job when run_async receives circuits and shots. | event_driven | Schnittstelle | nein | indirect |
| QR-0665-15 | The Backend class shall provide a synchronous run(circuits, shots) wrapper. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0665-16 | When given a submitted job identifier, the Backend class shall retrieve the corresponding job. | event_driven | Schnittstelle | nein | indirect |
| QR-0665-17 | The Job class shall track the lifecycle of a single execution. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0665-18 | When dispatch() is called, the BatchedBackend class shall execute circuits queued through run(). | event_driven | Schnittstelle | nein | indirect |
| QR-0665-19 | The PassManager class shall run its ordered CircuitPass instances through run(qc). | ubiquitous | Schnittstelle | nein | indirect |
| QR-0665-20 | The PassManager class shall verify circuit correctness through verify(qc). | ubiquitous | Schnittstelle | nein | indirect |
| QR-0665-21 | The dicke_state function shall prepare Dicke states deterministically. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0665-22 | The unbalanced_w_state function shall prepare unbalanced W states deterministically. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0665-23 | The QuantumArray class shall provide in-place arithmetic operations. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0665-24 | The QuantumArray class shall provide element-wise logical operations. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0665-25 | The QuantumArray class shall provide reductions through all() and any(). | ubiquitous | Schnittstelle | nein | indirect |

#### PR 668

[github.com/eclipse-qrisp/Qrisp/pull/668](https://github.com/eclipse-qrisp/Qrisp/pull/668) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0668-01 | qrisp_test.yml shall execute pytest using the paths selected by its test-group matrix. | ubiquitous | Prozess | nein | indirect |

#### PR 669

[github.com/eclipse-qrisp/Qrisp/pull/669](https://github.com/eclipse-qrisp/Qrisp/pull/669) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0669-01 | Qrisp shall use ruff as its code formatter. | ubiquitous | Prozess | nein | insufficient |
| QR-0669-02 | Qrisp shall support Python versions 3.11 and 3.12. | ubiquitous | Qualität (nicht funktional) | nein | indirect |
| QR-0669-03 | Where an optional dependency group is selected at installation time, Qrisp shall install the dependencies declared for the selected group. | optional_feature | Schnittstelle | nein | indirect |
| QR-0669-04 | Qrisp unit tests via Pytest shall execute pytest under Python 3.11 and Python 3.12. | ubiquitous | Prozess | nein | indirect |

#### PR 670

[github.com/eclipse-qrisp/Qrisp/pull/670](https://github.com/eclipse-qrisp/Qrisp/pull/670) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0670-01 | When a pull request triggers the Qrisp unit-test workflow, the Qrisp unit-test workflow shall check code formatting with Ruff. | event_driven | Prozess | nein | indirect |
| QR-0670-02 | Qrisp shall require Python versions greater than or equal to 3.11 and less than 3.13. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 671

[github.com/eclipse-qrisp/Qrisp/pull/671](https://github.com/eclipse-qrisp/Qrisp/pull/671) · 10 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0671-01 | Qrisp shall preserve its public API signatures. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0671-02 | When called with two arguments whose types are not Jaxpr and list, Jaspr shall raise TypeError. | event_driven | Schnittstelle | nein | indirect |
| QR-0671-03 | If constvars are provided without consts, then Jaspr shall raise ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0671-04 | If the last Jaspr input variable is not a QuantumState, then Jaspr shall raise ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0671-05 | If the last Jaspr output variable is not a QuantumState, then Jaspr shall raise ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0671-06 | When conclude_tracing closes a tracing scope, TracingQuantumSession shall restore the abstract quantum state that was active before the scope. | event_driven | funktional/Leistung | nein | indirect |
| QR-0671-07 | If the abstract quantum state is outside the active JAX trace, then TracingQuantumSession shall raise an exception. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0671-08 | If classical bits are supplied to append in JAX mode, then TracingQuantumSession.append shall raise an exception. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0671-09 | If append receives a QuantumArray with a non-QuantumArray qubit argument, then TracingQuantumSession.append shall raise an exception. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0671-10 | If append receives QuantumArrays with different shapes, then TracingQuantumSession.append shall raise an exception. | unwanted_behaviour | Schnittstelle | nein | indirect |

#### PR 672

[github.com/eclipse-qrisp/Qrisp/pull/672](https://github.com/eclipse-qrisp/Qrisp/pull/672) · 9 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0672-01 | PRXGate shall implement PRX(alpha, beta) as RZ(beta) · RX(alpha) · RZ(-beta). | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0672-02 | When inverse() is called, PRXGate shall return PRXGate(-alpha, beta). | event_driven | Schnittstelle | nein | indirect |
| QR-0672-03 | convert_to_prx shall convert arbitrary U3 single-qubit gates to PRX gates. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0672-04 | convert_to_prx shall preserve the exact unitary of a converted circuit. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0672-05 | When collect_gphases is enabled for a decomposed circuit containing GPhaseGate instructions, decompose shall replace the instructions with one accumulated gphase gate. | event_driven | funktional/Leistung | nein | indirect |
| QR-0672-06 | When collect_gphases is enabled and an accumulated gphase gate is emitted, decompose shall anchor the gate on the first qubit of the last instruction with num_qubits greater than zero. | event_driven | funktional/Leistung | nein | indirect |
| QR-0672-07 | When converting a Qrisp PRXGate to Qiskit, the Qiskit converter shall create RGate(alpha, beta). | event_driven | Schnittstelle | nein | indirect |
| QR-0672-08 | When converting a Qiskit RGate to Qrisp, the Qiskit converter shall create PRXGate(alpha, beta). | event_driven | Schnittstelle | nein | indirect |
| QR-0672-09 | When converting a Qiskit circuit with a nonzero global phase, the Qiskit converter shall add the corresponding Qrisp gphase gate. | event_driven | Schnittstelle | nein | indirect |

#### PR 674

[github.com/eclipse-qrisp/Qrisp/pull/674](https://github.com/eclipse-qrisp/Qrisp/pull/674) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0674-01 | The Ruff format job shall check formatting. | ubiquitous | Prozess | nein | indirect |

#### PR 675

[github.com/eclipse-qrisp/Qrisp/pull/675](https://github.com/eclipse-qrisp/Qrisp/pull/675) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0675-01 | Qrisp source code shall conform to Ruff formatting. | ubiquitous | Qualität (nicht funktional) | nein | indirect |
| QR-0675-02 | Ruff shall use a line length of 88 characters. | ubiquitous | Prozess | nein | indirect |
| QR-0675-03 | Ruff shall target Python 3.12. | ubiquitous | Prozess | nein | indirect |
| QR-0675-04 | The Ruff formatter shall use double quotes. | ubiquitous | Prozess | nein | indirect |
| QR-0675-05 | The workflow shall run Ruff. | ubiquitous | Prozess | nein | direct |
| QR-0675-06 | convert_to_prx shall convert single-qubit gates to native PRX (Phased-RX) gates. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 676

[github.com/eclipse-qrisp/Qrisp/pull/676](https://github.com/eclipse-qrisp/Qrisp/pull/676) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0676-01 | The Ruff format step shall check source formatting. | ubiquitous | Prozess | nein | indirect |
| QR-0676-02 | The dev dependency group shall include Ruff version 0.15.16. | ubiquitous | Prozess | nein | indirect |
| QR-0676-03 | The Ruff configuration shall set line-length to 120. | ubiquitous | Prozess | nein | indirect |

#### PR 677

[github.com/eclipse-qrisp/Qrisp/pull/677](https://github.com/eclipse-qrisp/Qrisp/pull/677) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0677-01 | The iqm optional-dependency extra shall require iqm-client[qiskit] version 33.0.3 or later. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0677-02 | The Install dependencies step shall install Qrisp with the dev, docs, iqm, catalyst, xdsl, aqt, and qiskit extras. | ubiquitous | Prozess | nein | indirect |

#### PR 678

[github.com/eclipse-qrisp/Qrisp/pull/678](https://github.com/eclipse-qrisp/Qrisp/pull/678) · 12 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0678-01 | Qrisp shall support Python versions 3.11 through 3.13. | ubiquitous | Qualität (nicht funktional) | nein | indirect |
| QR-0678-02 | The Qrisp package shall declare these core dependency version ranges: numba >=0.61,<0.66; networkx >=3.5,<4; tqdm >=4.67,<5; dill >=0.4.0,<0.5; psutil >=7.0.0,<8. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0678-03 | When the aqt optional dependency group is installed, the Qrisp package shall require pytest-httpx version >=0.36.0 and <0.37. | event_driven | Schnittstelle | nein | indirect |
| QR-0678-04 | When the cirq optional dependency group is installed, the Qrisp package shall require cirq version >=1.3 and <1.6. | event_driven | Schnittstelle | nein | indirect |
| QR-0678-05 | When the qiskit optional dependency group is installed, the Qrisp package shall require qiskit-aer version >=0.16 and <0.18. | event_driven | Schnittstelle | nein | indirect |
| QR-0678-06 | When the qiskit optional dependency group is installed, the Qrisp package shall require qiskit-ibm-runtime version >=0.44 and <0.45. | event_driven | Schnittstelle | nein | indirect |
| QR-0678-07 | When the catalyst optional dependency group is installed, the Qrisp package shall require pennylane version >=0.45 and <0.46. | event_driven | Schnittstelle | nein | indirect |
| QR-0678-08 | When the dev-testing optional dependency group is installed, the Qrisp package shall require pyscf version >=2.13 and <2.14. | event_driven | Schnittstelle | nein | indirect |
| QR-0678-09 | When the dev-testing optional dependency group is installed, the Qrisp package shall require tqecd version >=0.2.0 and <0.3. | event_driven | Schnittstelle | nein | indirect |
| QR-0678-10 | The development guide shall instruct developers to install development dependencies with the dev optional dependency group. | ubiquitous | Prozess | nein | indirect |
| QR-0678-11 | When installing dependencies, CI shall install the dev, catalyst, xdsl, and iqm optional dependency groups. | event_driven | Prozess | nein | direct |
| QR-0678-12 | The ruff workflow shall run using Python version 3.12.*. | ubiquitous | Prozess | nein | indirect |

#### PR 679

[github.com/eclipse-qrisp/Qrisp/pull/679](https://github.com/eclipse-qrisp/Qrisp/pull/679) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0679-01 | The classical-to-LLVM lowering pass shall convert operations from the arith, tensor, scf, and math MLIR dialects into the llvm dialect. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0679-02 | classical_to_llvm shall leave jasp operations unchanged. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 682

[github.com/eclipse-qrisp/Qrisp/pull/682](https://github.com/eclipse-qrisp/Qrisp/pull/682) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0682-01 | When qubitizing a non-Hermitian block-encoding of a Hermitian matrix, BlockEncoding.qubitization() shall construct a strictly Hermitian walk operator. | event_driven | funktional/Leistung | nein | indirect |
| QR-0682-02 | When the Hamiltonian-simulation time parameter t is large, Hamiltonian simulation shall compute Jacobi-Anger expansion coefficients without numerical overflow. | event_driven | funktional/Leistung | nein | indirect |
| QR-0682-03 | jax_jv shall execute under JAX tracing. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0682-04 | jax_jv shall be differentiable. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0682-05 | jax_jv shall be jaspify-compatible. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 683

[github.com/eclipse-qrisp/Qrisp/pull/683](https://github.com/eclipse-qrisp/Qrisp/pull/683) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0683-01 | Qrisp shall support Python 3.13. | ubiquitous | funktional/Leistung | nein | direct |
| QR-0683-02 | When the on-push trigger occurs, the pipeline shall run for Python 3.13. | event_driven | Prozess | nein | direct |

#### PR 684

[github.com/eclipse-qrisp/Qrisp/pull/684](https://github.com/eclipse-qrisp/Qrisp/pull/684) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0684-01 | The Code style checks workflow shall run Ruff formatting validation separately from the Qrisp test workflow. | ubiquitous | Prozess | nein | indirect |
| QR-0684-02 | When a pull request targets main, the Code style checks workflow shall run Ruff formatting validation. | event_driven | Prozess | nein | indirect |
| QR-0684-03 | When changes are pushed to main, the Code style checks workflow shall run Ruff formatting validation. | event_driven | Prozess | nein | indirect |

#### PR 685

[github.com/eclipse-qrisp/Qrisp/pull/685](https://github.com/eclipse-qrisp/Qrisp/pull/685) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0685-01 | The Qrisp test workflow shall cache pip dependencies. | ubiquitous | Prozess | nein | indirect |

#### PR 686

[github.com/eclipse-qrisp/Qrisp/pull/686](https://github.com/eclipse-qrisp/Qrisp/pull/686) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0686-01 | When U is non-Hermitian, the tilde U operator shall encode (A + A†)/2 as a Hermitian block encoding. | event_driven | funktional/Leistung | nein | indirect |
| QR-0686-02 | When U is non-Hermitian, the tilde U operator shall require one additional ancilla qubit. | event_driven | funktional/Leistung | nein | indirect |

#### PR 687

[github.com/eclipse-qrisp/Qrisp/pull/687](https://github.com/eclipse-qrisp/Qrisp/pull/687) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0687-01 | The Dependabot configuration shall schedule weekly update checks for GitHub Actions dependencies in the repository root. | ubiquitous | Schnittstelle | **ja** | indirect |
| QR-0687-02 | The Dependabot configuration shall schedule weekly update checks for pip dependencies in the repository root. | ubiquitous | Schnittstelle | **ja** | indirect |
| QR-0687-03 | The Dependabot configuration shall limit open update pull requests to 10 for each configured package ecosystem. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0687-04 | The Dependabot configuration shall apply the "dependabot-dependency-upgrade" label to Dependabot update pull requests. | ubiquitous | Schnittstelle | nein | direct |
| QR-0687-05 | When Dependabot opens an update pull request, Qrisp shall leave the merge decision to a human. | event_driven | Prozess | **ja** | insufficient |

#### PR 690

[github.com/eclipse-qrisp/Qrisp/pull/690](https://github.com/eclipse-qrisp/Qrisp/pull/690) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0690-01 | The documentation/source/index.rst landing-page example shall use Qiskit simulation APIs available in Qiskit 2.x. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0690-02 | The quantum_arithmetic_example.py example shall use Qiskit simulation APIs available in Qiskit 2.x. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0690-03 | The unitary_calculation.py example shall use Qiskit simulation APIs available in Qiskit 2.x. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 691

[github.com/eclipse-qrisp/Qrisp/pull/691](https://github.com/eclipse-qrisp/Qrisp/pull/691) · 7 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0691-01 | Jaspr.to_quake_mlir shall compile a Jaspr into a Quake-dialect MLIR string. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0691-02 | When execution_mode is "run", Jaspr.to_quake_mlir shall preserve classical return values in the generated function signature. | event_driven | Schnittstelle | nein | indirect |
| QR-0691-03 | When execution_mode is "sample", Jaspr.to_quake_mlir shall generate a function with a void return type. | event_driven | Schnittstelle | nein | indirect |
| QR-0691-04 | cudaq_kernel_from_mlir shall compile a Quake MLIR string into a callable CUDA-Q kernel. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0691-05 | If FixedShapeNDArray receives an unsupported dtype, then FixedShapeNDArray shall raise a TypeError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0691-06 | If FixedShapeNDArray receives a size that is not a positive integer, then FixedShapeNDArray shall raise a ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0691-07 | Where cudaq is not installed, qrisp.jasp.cudaq_interface shall raise an ImportError when imported. | optional_feature | Schnittstelle | nein | indirect |

#### PR 692

[github.com/eclipse-qrisp/Qrisp/pull/692](https://github.com/eclipse-qrisp/Qrisp/pull/692) · 8 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0692-01 | Jaspr.to_quake_mlir shall compile a Jaspr to MLIR using the Quake dialect. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0692-02 | Where execution_mode is "run", Jaspr.to_quake_mlir shall preserve classical return values in the function signature. | optional_feature | Schnittstelle | nein | indirect |
| QR-0692-03 | Where execution_mode is "sample", Jaspr.to_quake_mlir shall generate a kernel with a void return type. | optional_feature | Schnittstelle | nein | indirect |
| QR-0692-04 | cudaq_kernel_from_mlir shall compile a Quake MLIR string into a callable CUDA-Q kernel. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0692-05 | Where cudaq is not installed, qrisp.jasp.cudaq_interface shall raise ImportError when imported. | optional_feature | Schnittstelle | nein | indirect |
| QR-0692-06 | If FixedShapeNDArray receives an unsupported dtype, then FixedShapeNDArray shall reject the dtype by raising TypeError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0692-07 | If FixedShapeNDArray receives a size that is not a positive integer, then FixedShapeNDArray shall reject the size by raising ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0692-08 | The Qrisp CUDA-Q extra shall declare cudaq>=0.14.0 as a dependency. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 693

[github.com/eclipse-qrisp/Qrisp/pull/693](https://github.com/eclipse-qrisp/Qrisp/pull/693) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0693-01 | Where cudaq is not installed, when qrisp.jasp.cudaq_interface is imported, qrisp.jasp.cudaq_interface shall raise an ImportError. | complex | Schnittstelle | nein | indirect |
| QR-0693-02 | If FixedShapeNDArray receives a dtype other than float, int, or bool, then FixedShapeNDArray shall raise a TypeError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0693-03 | If FixedShapeNDArray receives a size that is not a positive integer, then FixedShapeNDArray shall raise a ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0693-04 | Jaspr.to_quake_mlir shall compile a Jaspr into MLIR using the Quake dialect. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0693-05 | cudaq_kernel_from_mlir shall compile a Quake MLIR string into a callable CUDA-Q kernel. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0693-06 | When cudaq_kernel_from_mlir is called with execution_mode="sample", cudaq_kernel_from_mlir shall produce a void-return CUDA-Q kernel. | event_driven | Schnittstelle | nein | indirect |

#### PR 694

[github.com/eclipse-qrisp/Qrisp/pull/694](https://github.com/eclipse-qrisp/Qrisp/pull/694) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0694-01 | When CreateQubitsOp is assembled, CreateQubitsOp shall emit the amount type before the quantum-state type in its operand type list. | event_driven | Schnittstelle | nein | indirect |

#### PR 699

[github.com/eclipse-qrisp/Qrisp/pull/699](https://github.com/eclipse-qrisp/Qrisp/pull/699) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0699-01 | When introducing the quantum oracle's second register, the QC basics tutorial shall explain that ⊕ denotes addition modulo 2. | event_driven | Gebrauchstauglichkeit | nein | direct |
| QR-0699-02 | When stating that a classical solution needs N/2+1 queries, the QC basics tutorial shall explain the query count. | event_driven | Gebrauchstauglichkeit | nein | direct |
| QR-0699-03 | When expanding the Hadamard transform of ±\|+⟩, the QC basics tutorial shall state that the two ± signs represent the same operator. | event_driven | Gebrauchstauglichkeit | nein | direct |
| QR-0699-04 | The QC basics tutorial shall define the imaginary unit as i² = -1. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0699-05 | The QC basics tutorial shall describe an eigenvalue as scaling its eigenvector in the same way as its matrix. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 701

[github.com/eclipse-qrisp/Qrisp/pull/701](https://github.com/eclipse-qrisp/Qrisp/pull/701) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0701-01 | RYYGate shall return a two-qubit Ising YY-coupling operation whose unitary equals exp(-i*phi/2 * Y (x) Y). | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0701-02 | When QuantumCircuit.ryy is called with a nonzero angle, QuantumCircuit shall append an RYY gate to the two supplied qubits. | event_driven | Schnittstelle | nein | indirect |
| QR-0701-03 | While tracing mode is active, when ryy is invoked, ryy shall append an RYY operation with the supplied phase as a traced parameter. | complex | Schnittstelle | nein | indirect |
| QR-0701-04 | When a circuit containing an RYY gate is converted to Qiskit and then converted back, the qiskit converters shall preserve the circuit unitary. | event_driven | Schnittstelle | nein | indirect |
| QR-0701-05 | The pennylane converters shall map RYYGate to qml.IsingYY. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 702

[github.com/eclipse-qrisp/Qrisp/pull/702](https://github.com/eclipse-qrisp/Qrisp/pull/702) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0702-01 | The QFT subchapter shall provide additional explanation of the Quantum Fourier Transform. | ubiquitous | Prozess | nein | direct |
| QR-0702-02 | The Quantum Fourier Transform shall have a worst-case run time of O(n log n). | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0702-03 | The inverse Quantum Fourier Transformation shall be denoted IQFT in its defining equation. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 705

[github.com/eclipse-qrisp/Qrisp/pull/705](https://github.com/eclipse-qrisp/Qrisp/pull/705) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0705-01 | RYYGate shall return an Ising YY-coupling operation whose unitary equals exp(-i·φ/2·Y⊗Y). | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0705-02 | When called with a nonzero angle, QuantumCircuit.ryy shall append an RYYGate with that angle to the specified two qubits. | event_driven | Schnittstelle | nein | indirect |
| QR-0705-03 | ryy shall apply an RYY gate with the supplied phase to the two supplied qubit arguments. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 706

[github.com/eclipse-qrisp/Qrisp/pull/706](https://github.com/eclipse-qrisp/Qrisp/pull/706) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0706-01 | When CI runs, the CI pipeline shall run codespell. | event_driven | Prozess | nein | indirect |
| QR-0706-02 | The Qrisp project shall enforce American English spelling. | ubiquitous | Prozess | nein | indirect |
| QR-0706-03 | If a breaking change has not been explicitly agreed on with the maintainers, then the Qrisp contribution process shall preserve existing user-facing behavior. | unwanted_behaviour | Prozess | nein | direct |
| QR-0706-04 | When a line contains embedded base64 image data, the codespell configuration shall ignore the line. | event_driven | Prozess | nein | indirect |

#### PR 709

[github.com/eclipse-qrisp/Qrisp/pull/709](https://github.com/eclipse-qrisp/Qrisp/pull/709) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0709-01 | When constructing a Cirq CircuitOperation, test_cirq_converter.py shall preserve current repetition-ID behavior without triggering the Cirq FutureWarning. | event_driven | Schnittstelle | nein | indirect |

#### PR 711

[github.com/eclipse-qrisp/Qrisp/pull/711](https://github.com/eclipse-qrisp/Qrisp/pull/711) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0711-01 | The Development Guide shall display the Qrisp Development Guide image. | ubiquitous | Prozess | nein | indirect |

#### PR 712

[github.com/eclipse-qrisp/Qrisp/pull/712](https://github.com/eclipse-qrisp/Qrisp/pull/712) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0712-01 | When the CI test workflow runs a pytest test group, the CI test workflow shall generate a terminal report identifying qrisp lines that lack unit-test coverage. | event_driven | Prozess | nein | indirect |
| QR-0712-02 | When the CI test workflow runs a pytest test group, the CI test workflow shall collect branch coverage for the qrisp package. | event_driven | Prozess | nein | indirect |
| QR-0712-03 | The coverage configuration shall exclude files that match */__init__.py. | ubiquitous | Prozess | nein | indirect |

#### PR 715

[github.com/eclipse-qrisp/Qrisp/pull/715](https://github.com/eclipse-qrisp/Qrisp/pull/715) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0715-01 | When posting a pull-request comment through the Issues API, the changelog workflow shall use issues write permission. | event_driven | Schnittstelle | **ja** | indirect |
| QR-0715-02 | When a pull request diff modifies a numeric major.minor changelog file in documentation/source/general/changelog, the changelog workflow shall report that the changelog was modified. | event_driven | funktional/Leistung | nein | indirect |

#### PR 716

[github.com/eclipse-qrisp/Qrisp/pull/716](https://github.com/eclipse-qrisp/Qrisp/pull/716) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0716-01 | The repository landing page shall display a note that the project is under active development. | ubiquitous | Gebrauchstauglichkeit | nein | indirect |

#### PR 727

[github.com/eclipse-qrisp/Qrisp/pull/727](https://github.com/eclipse-qrisp/Qrisp/pull/727) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0727-01 | When a pull-request event is initiated by dependabot[bot], the changelog workflow shall omit the remind job. | event_driven | Prozess | nein | direct |

#### PR 739

[github.com/eclipse-qrisp/Qrisp/pull/739](https://github.com/eclipse-qrisp/Qrisp/pull/739) · 7 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0739-01 | sample shall accept sampling kernels that return arbitrary values. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0739-02 | expectation_value shall accept sampling kernels that return arbitrary values. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0739-03 | sample shall automatically measure and decode QuantumVariables returned by a sampling kernel. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0739-04 | expectation_value shall automatically measure and decode QuantumVariables returned by a sampling kernel. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0739-05 | When terminal_sampling=True is used with a sampling kernel that returns classical values, terminal_sampling shall raise a ValueError. | event_driven | Schnittstelle | nein | indirect |
| QR-0739-06 | sample shall require sampling kernels to receive only classical arguments. | ubiquitous | Schnittstelle | nein | direct |
| QR-0739-07 | expectation_value shall require sampling kernels to receive only classical arguments. | ubiquitous | Schnittstelle | nein | direct |

#### PR 740

[github.com/eclipse-qrisp/Qrisp/pull/740](https://github.com/eclipse-qrisp/Qrisp/pull/740) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0740-01 | During refactoring, mcx shall retain its existing behavior. | state_driven | Schnittstelle | nein | indirect |

#### PR 743

[github.com/eclipse-qrisp/Qrisp/pull/743](https://github.com/eclipse-qrisp/Qrisp/pull/743) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0743-01 | The Link Checker shall check links in .rst documentation and Python docstrings. | ubiquitous | Prozess | nein | indirect |
| QR-0743-02 | The Link Checker shall check links in README.md, Markdown files under src, the pull request template, Python files under src, and Python test files. | ubiquitous | Prozess | nein | indirect |

#### PR 745

[github.com/eclipse-qrisp/Qrisp/pull/745](https://github.com/eclipse-qrisp/Qrisp/pull/745) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0745-01 | The dev-testing dependency group shall include pytest-benchmark version 5.1.0 or later. | ubiquitous | Prozess | nein | indirect |
| QR-0745-02 | When QRISP_BENCHMARK_ALL is enabled, the pytest configuration shall benchmark collected tests without fixture arguments. | event_driven | Prozess | nein | indirect |
| QR-0745-03 | While QRISP_BENCHMARK_ALL is enabled, when a collected test is under jax_tests/, the pytest configuration shall execute the test with one benchmark round and one iteration. | complex | Prozess | nein | indirect |
| QR-0745-04 | The CI workflow shall automatically save benchmark results. | ubiquitous | Prozess | nein | indirect |
| QR-0745-05 | The CI workflow shall compare benchmark results against saved baselines. | ubiquitous | Prozess | nein | indirect |
| QR-0745-06 | If a benchmark regression exceeds 5%, then the CI workflow shall fail the benchmark run. | unwanted_behaviour | Prozess | nein | indirect |

#### PR 756

[github.com/eclipse-qrisp/Qrisp/pull/756](https://github.com/eclipse-qrisp/Qrisp/pull/756) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0756-01 | When converting a Qrisp circuit containing an SX operation, including a controlled instance, to Qiskit, Qrisp shall preserve the operation's exact unitary. | event_driven | Schnittstelle | nein | direct |
| QR-0756-02 | When converting a Qrisp circuit containing an SX-dagger operation, including a controlled instance, to Qiskit, Qrisp shall preserve the operation's exact unitary. | event_driven | Schnittstelle | nein | direct |
| QR-0756-03 | When importing a Qiskit SX operation, including a controlled instance, Qrisp shall preserve the operation's exact unitary. | event_driven | Schnittstelle | nein | direct |
| QR-0756-04 | When importing a Qiskit SX-dagger operation, including a controlled instance, Qrisp shall preserve the operation's exact unitary. | event_driven | Schnittstelle | nein | direct |
| QR-0756-05 | When importing a Qiskit operation named `sxdg`, Qrisp shall map the operation to `sx_dg`. | event_driven | Schnittstelle | nein | direct |

#### PR 757

[github.com/eclipse-qrisp/Qrisp/pull/757](https://github.com/eclipse-qrisp/Qrisp/pull/757) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0757-01 | When the IQM package is installed, qrisp.interface.provider_backends.iqm_backend shall make IQMBackend available. | event_driven | Schnittstelle | nein | indirect |
| QR-0757-02 | IQMBackend shall be a subclass of qrisp.interface.Backend. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0757-03 | When the IQM package is not installed, _MissingIQMBackend shall raise an ImportError that instructs the caller to install qrisp[iqm] upon instantiation. | event_driven | Schnittstelle | nein | indirect |
| QR-0757-04 | IQMBackend shall execute circuits on IQM quantum hardware. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0757-05 | The iqm optional dependency group shall include iqm-client[qrisp]. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 759

[github.com/eclipse-qrisp/Qrisp/pull/759](https://github.com/eclipse-qrisp/Qrisp/pull/759) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0759-01 | check_synthesis shall resolve the int_encoder symbol. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0759-02 | synth_poly shall return the synthesized polynomial. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 769

[github.com/eclipse-qrisp/Qrisp/pull/769](https://github.com/eclipse-qrisp/Qrisp/pull/769) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0769-01 | When qswitch state preparation is followed by its inverse in Jasp mode, Jasp shall restore the target quantum variable to the \|0> state. | event_driven | funktional/Leistung | nein | direct |
| QR-0769-02 | When qswitch state preparation and its inverse execute inside a control environment whose control qubit is \|1> in Jasp mode, Jasp shall restore the target quantum variable to the \|0> state. | event_driven | funktional/Leistung | nein | direct |
| QR-0769-03 | When a control qubit is in an equal superposition during qswitch state preparation in Jasp mode, Jasp shall return a probability distribution with equal contributions from the \|0> target state and the prepared distribution. | event_driven | funktional/Leistung | nein | direct |

#### PR 774

[github.com/eclipse-qrisp/Qrisp/pull/774](https://github.com/eclipse-qrisp/Qrisp/pull/774) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0774-01 | The Coverage workflow shall execute separately from the testing pipeline. | ubiquitous | Prozess | nein | direct |
| QR-0774-02 | When new functionality is added to Qrisp, Qrisp shall fully cover the new functionality with unit tests. | event_driven | Prozess | nein | direct |
| QR-0774-03 | The Coverage workflow shall report missing coverage for the qrisp package. | ubiquitous | Prozess | nein | indirect |

#### PR 788

[github.com/eclipse-qrisp/Qrisp/pull/788](https://github.com/eclipse-qrisp/Qrisp/pull/788) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0788-01 | When submitting circuits, QiskitBackend shall invoke the wrapped backend's run() method. | event_driven | Schnittstelle | nein | indirect |
| QR-0788-02 | When processing a Qiskit Result, QiskitJob shall obtain per-circuit counts through Result.get_counts(). | event_driven | Schnittstelle | nein | indirect |
| QR-0788-03 | When submitting circuits to IBM Runtime, QiskitRuntimeBackend shall use SamplerV2. | event_driven | Schnittstelle | nein | indirect |
| QR-0788-04 | When a real IBM Quantum backend is provided, QiskitBackend shall raise a TypeError directing the caller to QiskitRuntimeBackend. | event_driven | Schnittstelle | nein | indirect |
| QR-0788-05 | If a backend run result lacks get_counts(), then QiskitJob shall raise a TypeError identifying _extract_counts(). | unwanted_behaviour | Schnittstelle | nein | indirect |

#### PR 791

[github.com/eclipse-qrisp/Qrisp/pull/791](https://github.com/eclipse-qrisp/Qrisp/pull/791) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0791-01 | The tutorial shall use QiskitRuntimeBackend. | ubiquitous | Prozess | nein | direct |

### Pull Requests ohne Anforderungen

| PR | Status | Begründung des Modells |
|---|---|---|
| [5](https://github.com/eclipse-qrisp/Qrisp/pull/5) | keine Anforderungen gefunden | The pull request only corrects typos and Markdown, LaTeX, and formatting details in documentation. It states no behavioural, interface, quality, or process requirement for Qrisp. |
| [15](https://github.com/eclipse-qrisp/Qrisp/pull/15) | keine Anforderungen gefunden | The pull request contains documentation typo, wording, formatting, hyperlink, and equation-layout corrections only. It states no new or changed requirement for Qrisp behaviour or properties. |
| [75](https://github.com/eclipse-qrisp/Qrisp/pull/75) | keine Anforderungen gefunden | The pull request only removes documentation files and provides no statement of a required Qrisp behaviour, property, interface, or documentation rule. |
| [126](https://github.com/eclipse-qrisp/Qrisp/pull/126) | keine Anforderungen gefunden | The material only shows documentation-example corrections, formatting changes, added imports, and an adjusted sample parameter. It does not state a verifiable requirement on Qrisp behaviour or properties. |
| [257](https://github.com/eclipse-qrisp/Qrisp/pull/257) | keine Anforderungen gefunden | The pull request only identifies a typo correction. The changed notebook diff is unavailable, so no behavioural or property requirement is stated. |
| [285](https://github.com/eclipse-qrisp/Qrisp/pull/285) | keine Anforderungen gefunden | The pull request removes an unused code snippet and states no capability, behaviour, property, or process requirement for Qrisp. |
| [300](https://github.com/eclipse-qrisp/Qrisp/pull/300) | keine Anforderungen gefunden | The pull request only reports applying isort and Black formatting to source code and test files. It states no behavioural, interface, quality, or process requirement for Qrisp. |
| [320](https://github.com/eclipse-qrisp/Qrisp/pull/320) | keine Anforderungen gefunden | The pull request corrects a dependency-name typo. The comments state that the typo already caused the intended package to be installed through a dummy package, so the material does not establish a changed Qrisp requirement. |
| [407](https://github.com/eclipse-qrisp/Qrisp/pull/407) | Eingabe nicht verwertbar | The material contains only an unexplained title and no description, comments, or diff text from which requirements can be reconstructed. |
| [446](https://github.com/eclipse-qrisp/Qrisp/pull/446) | keine Anforderungen gefunden | The material describes a global Black formatting application and copyright-header updates. These are housekeeping changes and do not state a behavioural, interface, quality, or process requirement beyond formatting. |
| [447](https://github.com/eclipse-qrisp/Qrisp/pull/447) | keine Anforderungen gefunden | The pull request changes documentation content, labels, and research listings. It does not state a prescriptive requirement or a clearly intended behavioural or quality constraint for Qrisp. |
| [493](https://github.com/eclipse-qrisp/Qrisp/pull/493) | keine Anforderungen gefunden | The material only identifies a cleanup of the examples directory and the removal of a notebook; it states no behavioural or quality requirement. |
| [507](https://github.com/eclipse-qrisp/Qrisp/pull/507) | keine Anforderungen gefunden | The material only reports removal of tracked .pymon files and contains no behavioural, interface, quality, or process requirement. |
| [525](https://github.com/eclipse-qrisp/Qrisp/pull/525) | Eingabe nicht verwertbar | The material contains only a title and a file name; the notebook diff and any explanatory text are missing. |
| [554](https://github.com/eclipse-qrisp/Qrisp/pull/554) | keine Anforderungen gefunden | The pull request removes a template heading because of its presentation in pull requests. The material states no requirement on Qrisp's behaviour, properties, interfaces, or development process. |
| [559](https://github.com/eclipse-qrisp/Qrisp/pull/559) | keine Anforderungen gefunden | The pull request is explicitly classified as refactoring with no behavior change. The material only removes obsolete BoundQubitTerm and BoundQubitOperator implementation and its test coverage without stating a required Qrisp behavior or property. |
| [600](https://github.com/eclipse-qrisp/Qrisp/pull/600) | keine Anforderungen gefunden | The pull request only removes a folder described as accidentally introduced. It states no required Qrisp behavior or property. |
| [661](https://github.com/eclipse-qrisp/Qrisp/pull/661) | keine Anforderungen gefunden | The pull request only reorders existing Jaspr.to_mlir documentation text without changing its stated behaviour or adding a documented rule. |
| [737](https://github.com/eclipse-qrisp/Qrisp/pull/737) | keine Anforderungen gefunden | The material records a test changelog entry and removal of a README license section, but it states no requirement on Qrisp behaviour, interface, quality, or development process. |

### Nicht schemagültige Antworten (in der Arbeit nicht gezählt)

3 Antworten bestehen die Prüfung gegen `config/requirement_schema_v2.json` nicht. Ihre 12 Anforderungen sind in den Zahlen oben und in der Arbeit nicht enthalten; sie stehen hier nur der Vollständigkeit halber.

#### PR 555 (nicht schemagültig)

[github.com/eclipse-qrisp/Qrisp/pull/555](https://github.com/eclipse-qrisp/Qrisp/pull/555) · Schemafehler: 'ipykernel' is too short; 'stim' is too short

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0555-01 | The docs-install target shall install the Python documentation requirements. | ubiquitous | Prozess | nein | indirect |
| QR-0555-02 | The docs-install target shall install the pandoc system package. | ubiquitous | Prozess | nein | indirect |
| QR-0555-03 | The Qrisp documentation build shall require a Sphinx version from 7 inclusive through 9 exclusive. | ubiquitous | Prozess | nein | indirect |
| QR-0555-04 | The local Qrisp package shall be importable by autodoc and autosummary. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0555-05 | The Qrisp documentation build shall have ipykernel available. | ubiquitous | Prozess | nein | indirect |
| QR-0555-06 | The Qrisp documentation build shall have stim available. | ubiquitous | Prozess | nein | indirect |
| QR-0555-07 | The documentation configuration shall configure the Lovelace light Pygments style with pygments_light_style. | ubiquitous | Qualität (nicht funktional) | nein | indirect |
| QR-0555-08 | The documentation README shall instruct contributors to run make docs-install before make html. | ubiquitous | Prozess | nein | indirect |

#### PR 688 (nicht schemagültig)

[github.com/eclipse-qrisp/Qrisp/pull/688](https://github.com/eclipse-qrisp/Qrisp/pull/688) · Schemafehler: [{'location': 'diff', 'locator': '.github/workflows/docs_build.yml', 'html_url': None, 'ex

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0688-01 | When a pull request changes a file selected by the Docs Build path filters, Docs Build shall build HTML documentation. | event_driven | Prozess | nein | indirect |
| QR-0688-02 | When Docs Build runs for a pull request, Docs Build shall publish the generated HTML under pr-<pull request number> on the gh-pages branch. | event_driven | Prozess | nein | indirect |
| QR-0688-03 | When Docs Build runs for a pull request, Docs Build shall post the documentation preview URL as a comment on the pull request. | event_driven | Prozess | nein | indirect |
| QR-0688-04 | If no GitHub Pages site exists, then Docs Build shall create a GitHub Pages site sourced from the gh-pages branch root. | unwanted_behaviour | Prozess | nein | indirect |

#### PR 796 (nicht schemagültig)

[github.com/eclipse-qrisp/Qrisp/pull/796](https://github.com/eclipse-qrisp/Qrisp/pull/796) · Schemafehler: 'requirements' is a required property

_Keine Anforderungen im Datensatz._

## Teil 2: Anthropic claude-sonnet-5-5 (Vergleichslauf)

Explorativer Vergleichslauf vom 21. Oktober 2026 an denselben 20 Pull Requests der Bewertung, mit unveränderter Anweisung v2 (thesis.pdf, Abschnitt 6.3.3, S. 61; Tabelle 6.5, S. 62: 68 Anforderungen). Keine Bewertung von Hand.

| Angabe | Wert |
|---|---|
| Modell (Manifest) | `claude-sonnet-5-5` |
| Quelldatei | `data/processed/extraction_2026-10-21_claude_eval_v2.jsonl` |
| SHA-256 der Quelldatei | `891b8ead181cc40fdae3c81dd012a917f6f938f01080145f33c485469058beb6` |
| Code-Commit des Laufs | `2e8fbed9ae8d89f8d755b4b14f4269b884710ae9` |
| Antworten / davon schemagültig | 20 / 20 |
| Pull Requests mit Anforderungen | 17 |
| Anforderungen (schemagültige Antworten) | 68 |
| davon sicherheitsrelevant (Modellangabe) | 0 |
| Typ: funktional/Leistung | 34 |
| Typ: Schnittstelle | 25 |
| Typ: Qualität (nicht funktional) | 5 |
| Typ: Prozess | 2 |
| Typ: Gebrauchstauglichkeit | 2 |

### Anforderungen je Pull Request

#### PR 38

[github.com/eclipse-qrisp/Qrisp/pull/38](https://github.com/eclipse-qrisp/Qrisp/pull/38) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0038-01 | When visualize_cost is called after a simulation run, QAOAProblem.visualize_cost shall plot the recorded cost values against the selected gamma and beta parameters. | event_driven | funktional/Leistung | nein | indirect |
| QR-0038-02 | While the callback option is enabled, QAOAProblem shall record the classical cost value of each optimizer evaluation in its optimization_cost attribute. | state_driven | funktional/Leistung | nein | indirect |
| QR-0038-03 | QAOAProblem shall record the parameter vector of each optimizer iteration in its optimization_params attribute. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0038-04 | If visualize_cost is called on a QAOAProblem instance whose callback is not enabled, then QAOAProblem.visualize_cost shall raise an exception. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0038-05 | If a layer index passed to visualize_cost exceeds the depth of the QAOA instance, then QAOAProblem.visualize_cost shall raise an exception. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0038-06 | When QAOAProblem runs its parameter optimization, QAOAProblem shall execute the optimization loop only once, without a second iteration. | event_driven | funktional/Leistung | nein | insufficient |

#### PR 158

[github.com/eclipse-qrisp/Qrisp/pull/158](https://github.com/eclipse-qrisp/Qrisp/pull/158) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0158-01 | The Jaspr class shall place the quantum circuit at the last position of its argument and return signature. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0158-02 | Qrisp shall preserve the documented frontend interface across the change of the Jaspr signature. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 193

[github.com/eclipse-qrisp/Qrisp/pull/193](https://github.com/eclipse-qrisp/Qrisp/pull/193) · 1 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0193-01 | The qswitch function shall call mcx with the method name balauca when it compiles the switch-case structure in the branch that uses a conjugator. | ubiquitous | funktional/Leistung | nein | insufficient |

#### PR 209

[github.com/eclipse-qrisp/Qrisp/pull/209](https://github.com/eclipse-qrisp/Qrisp/pull/209) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0209-01 | The Qrisp documentation shall include a tutorial on the Linear Combination of Unitaries protocol and its applications. | ubiquitous | Prozess | nein | indirect |
| QR-0209-02 | The Qrisp documentation build shall render embedded YouTube videos in tutorial pages. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0209-03 | The inner_LCU function shall return the ancilla variable and the transformed target variable without measuring the ancilla variable. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0209-04 | If the unitaries argument is callable and num_unitaries is not specified, then the inner_LCU function shall raise a ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |

#### PR 230

[github.com/eclipse-qrisp/Qrisp/pull/230](https://github.com/eclipse-qrisp/Qrisp/pull/230) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0230-01 | The isqrt_alg function shall compute the integer square root of a QuantumFloat input and return it as a QuantumFloat. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0230-02 | The isqrt_alg function shall transform the input QuantumFloat into the remainder of the integer square root computation. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0230-03 | The isqrt_alg function shall compute the square root and the remainder without leaving garbage qubits. | ubiquitous | Qualität (nicht funktional) | nein | indirect |
| QR-0230-04 | The isqrt_alg function shall use a T-count optimized circuit for computing the integer square root. | ubiquitous | Qualität (nicht funktional) | nein | indirect |
| QR-0230-05 | The qrisp.algorithms package shall expose the isqrt module. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 361

[github.com/eclipse-qrisp/Qrisp/pull/361](https://github.com/eclipse-qrisp/Qrisp/pull/361) · 8 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0361-01 | The QuantumCircuit.to_stim method shall convert a QuantumCircuit into a stim.Circuit. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0361-02 | Qrisp shall translate classically controlled Pauli gates into Stim circuit instructions during conversion to Stim. | ubiquitous | funktional/Leistung | nein | direct |
| QR-0361-03 | When a parity operation is marked as an observable, the QuantumCircuit.to_stim method shall emit an OBSERVABLE_INCLUDE instruction in the Stim circuit. | event_driven | funktional/Leistung | nein | direct |
| QR-0361-04 | While the compilation target is not Stim, the StimNoiseGate class shall behave as a unitary identity gate. | state_driven | funktional/Leistung | nein | indirect |
| QR-0361-05 | The parity function shall compute the XOR of multiple measurement results. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0361-06 | The QuantumCircuit.parity method shall accept an expected parity value of 0 or 1 for the created parity check. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0361-07 | The extract_stim decorator shall return the Stim circuit that corresponds to the decorated Jasp-traceable quantum function. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0361-08 | The StimBackend function shall return a BatchedBackend that simulates Qrisp QuantumCircuits with Stim. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 405

[github.com/eclipse-qrisp/Qrisp/pull/405](https://github.com/eclipse-qrisp/Qrisp/pull/405) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0405-01 | The IQMBackend function shall accept a calibration set identifier that selects the calibration set used by the created backend. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0405-02 | Where the use_metrics parameter is set to True, the IQMBackend function shall create a backend that queries the server for calibration data and quality metrics and passes them to the transpilation targets. | optional_feature | funktional/Leistung | nein | indirect |
| QR-0405-03 | When no calibration set identifier is given, the IQMBackend function shall query the IQM Server for the current default calibration set. | event_driven | funktional/Leistung | nein | indirect |

#### PR 443

[github.com/eclipse-qrisp/Qrisp/pull/443](https://github.com/eclipse-qrisp/Qrisp/pull/443) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0443-01 | The Qrisp tutorial landing page shall group the tutorials into four topic sections. | ubiquitous | Gebrauchstauglichkeit | nein | indirect |
| QR-0443-02 | The Qrisp tutorial landing page shall inform readers that the tutorials can be downloaded as Jupyter notebooks. | ubiquitous | Gebrauchstauglichkeit | nein | indirect |

#### PR 445

[github.com/eclipse-qrisp/Qrisp/pull/445](https://github.com/eclipse-qrisp/Qrisp/pull/445) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0445-01 | Qrisp shall execute quantum variable name generation without relying on deprecated NumPy behaviour. | ubiquitous | Qualität (nicht funktional) | nein | indirect |
| QR-0445-02 | Qrisp shall compute the simulator's sparse vector inner product without relying on deprecated NumPy behaviour. | ubiquitous | Qualität (nicht funktional) | nein | indirect |

#### PR 461

[github.com/eclipse-qrisp/Qrisp/pull/461](https://github.com/eclipse-qrisp/Qrisp/pull/461) · 6 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0461-01 | When the translation_dic parameter is None, the extend method of QuantumCircuit shall map each qubit and clbit of the other circuit to the qubit or clbit with the same identifier. | event_driven | funktional/Leistung | nein | indirect |
| QR-0461-02 | If the num_qubits argument of the QuantumCircuit constructor is not an integer, then QuantumCircuit shall raise a TypeError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0461-03 | If the num_clbits argument of the QuantumCircuit constructor is not an integer, then QuantumCircuit shall raise a TypeError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0461-04 | If the translation of an instruction of the other circuit refers to a qubit that is not present in the extended circuit, then the extend method of QuantumCircuit shall raise an exception. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0461-05 | If the translation of an instruction of the other circuit refers to a clbit that is not present in the extended circuit, then the extend method of QuantumCircuit shall raise a ValueError. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0461-06 | Qrisp shall include a dedicated test file for the QuantumCircuit class. | ubiquitous | Prozess | nein | indirect |

#### PR 489

[github.com/eclipse-qrisp/Qrisp/pull/489](https://github.com/eclipse-qrisp/Qrisp/pull/489) · 7 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0489-01 | The QuantumCircuit.bind_parameters method shall return a QuantumCircuit whose abstract_params attribute is a set. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0489-02 | If the QuantumCircuit contains gates not representable in QASM 2.0, then the QuantumCircuit.to_qasm2 method shall export the transpiled circuit. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0489-03 | When the qubits argument of the QuantumCircuit.measure method is a tuple or a range, the method shall allocate one classical bit per qubit. | event_driven | funktional/Leistung | nein | indirect |
| QR-0489-04 | When the clbits argument of the QuantumCircuit.parity method is a tuple or another sequence of classical bits, the method shall treat it as multiple classical bits. | event_driven | funktional/Leistung | nein | indirect |
| QR-0489-05 | While xla_mode is below 2, the QuantumCircuit.add_clbit method shall skip the check for duplicate classical bit identifiers. | state_driven | Qualität (nicht funktional) | nein | indirect |
| QR-0489-06 | The QuantumCircuit.depth method shall return a value of type int. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0489-07 | When the parity of the classical bits matches the expected parity, the QuantumCircuit.parity method shall return the value 0. | event_driven | funktional/Leistung | nein | indirect |

#### PR 534

[github.com/eclipse-qrisp/Qrisp/pull/534](https://github.com/eclipse-qrisp/Qrisp/pull/534) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0534-01 | The jaxpr_to_xdsl function shall return a tuple of the xDSL Context and the xDSL module. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0534-02 | When to_mlir is called with lower_stablehlo=True, to_mlir shall produce an MLIR string that contains no linalg.generic operations. | event_driven | funktional/Leistung | nein | indirect |
| QR-0534-03 | The scalar_linalg_folding pass shall replace 0-dimensional linalg.generic operations with plain scalar arithmetic using tensor.extract and tensor.from_elements. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0534-04 | The scalar_tensor_folding pass shall replace a tensor.extract applied to a 0-dimensional tensor.from_elements with the underlying scalar value. | ubiquitous | funktional/Leistung | nein | indirect |
| QR-0534-05 | The cmpi_extui_folding pass shall fold comparisons of zero-extended booleans against the constants 0 or 1 into the original i1 value, its negation, or a constant true or false. | ubiquitous | funktional/Leistung | nein | indirect |

#### PR 587

[github.com/eclipse-qrisp/Qrisp/pull/587](https://github.com/eclipse-qrisp/Qrisp/pull/587) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0587-01 | If exact is set to True and winner_state_amount is not specified, then grovers_alg shall raise a ValueError. | unwanted_behaviour | Schnittstelle | nein | indirect |
| QR-0587-02 | When the oracle function acts on quantum variables that do not belong to args, grovers_alg shall execute without raising an exception. | event_driven | funktional/Leistung | nein | indirect |
| QR-0587-03 | The grovers_alg function shall accept the search-space quantum variables through a parameter named args. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 610

[github.com/eclipse-qrisp/Qrisp/pull/610](https://github.com/eclipse-qrisp/Qrisp/pull/610) · 5 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0610-01 | The QuantumCircuit.from_cirq method shall create a QuantumCircuit from a Cirq Circuit. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0610-02 | When a Qrisp circuit converted with to_cirq is converted back with QuantumCircuit.from_cirq, QuantumCircuit.from_cirq shall return a circuit with the same statevector as the original circuit. | event_driven | funktional/Leistung | nein | indirect |
| QR-0610-03 | If a Qrisp circuit contains a gate that is not supported by the converter, then convert_to_cirq shall raise a ValueError. | unwanted_behaviour | funktional/Leistung | nein | indirect |
| QR-0610-04 | When a Qrisp circuit contains gates that have no mapping to a Cirq gate, convert_to_cirq shall decompose those gates with Qrisp's transpiler before conversion. | event_driven | funktional/Leistung | nein | indirect |
| QR-0610-05 | Where the cirq_qubits parameter is provided, convert_to_cirq shall map the qubits of the Qrisp circuit to the given Cirq qubits. | optional_feature | Schnittstelle | nein | indirect |

#### PR 613

[github.com/eclipse-qrisp/Qrisp/pull/613](https://github.com/eclipse-qrisp/Qrisp/pull/613) · 2 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0613-01 | The FloatLike type alias shall exclude complex Python numbers and complex NumPy scalar types from the accepted gate parameter types. | ubiquitous | Schnittstelle | nein | indirect |
| QR-0613-02 | The FloatLike type alias shall accept NumPy floating-point scalars and NumPy integer scalars as gate parameter values. | ubiquitous | Schnittstelle | nein | indirect |

#### PR 650

[github.com/eclipse-qrisp/Qrisp/pull/650](https://github.com/eclipse-qrisp/Qrisp/pull/650) · 3 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0650-01 | The QubitOperator shall provide the method expectation_value, which takes a state_prep callable, as the method for evaluating the expected value of the operator. | ubiquitous | Schnittstelle | nein | direct |
| QR-0650-02 | The FermionicOperator shall provide the method expectation_value, which takes a state_prep callable, as the method for evaluating the expected value of the operator. | ubiquitous | Schnittstelle | nein | direct |
| QR-0650-03 | When expectation_value is called on the operator A(0)*C(1)*C(2)*A(3) + P1(0)*P1(2) + P1(1)*P1(3) with a state in which qubits 0 and 1 are set to one, the QubitOperator shall return the expectation value 0 for the diagonalisation methods commuting and commuting_qw. | event_driven | funktional/Leistung | nein | indirect |

#### PR 769

[github.com/eclipse-qrisp/Qrisp/pull/769](https://github.com/eclipse-qrisp/Qrisp/pull/769) · 4 Anforderung(en)

| ID | Anforderung | EARS-Muster | Typ | Sicherheit | Belegstärke |
|---|---|---|---|---|---|
| QR-0769-01 | When prepare is called with method="qswitch" inside an invert environment in Jasp mode, the prepare function shall apply the inverse of the state preparation. | event_driven | funktional/Leistung | nein | direct |
| QR-0769-02 | When prepare is called with method="qswitch" inside a control environment in Jasp mode, the prepare function shall apply the state preparation only on the branch where the control qubit is in state \|1>. | event_driven | funktional/Leistung | nein | direct |
| QR-0769-03 | When retracing a jit equation during the control transform introduces additional constvars, the control_eqn function shall pass the control qubit as the first argument followed by the original arguments of the equation in their original order. | event_driven | Schnittstelle | nein | direct |
| QR-0769-04 | When invert_eqn inverts a jit equation, invert_eqn shall produce an inverted Jaspr whose number of non-constant invars equals the number of invars supplied by the equation. | event_driven | Schnittstelle | nein | direct |

### Pull Requests ohne Anforderungen

| PR | Status | Begründung des Modells |
|---|---|---|
| [73](https://github.com/eclipse-qrisp/Qrisp/pull/73) | keine Anforderungen gefunden | The pull request only fixes documentation. It adds blank lines before code blocks, corrects wording and punctuation in the tutorials, and restructures the reference pages for the QAOA mixers. It states no capability, behaviour or property that Qrisp itself is required to have. |
| [300](https://github.com/eclipse-qrisp/Qrisp/pull/300) | keine Anforderungen gefunden | The pull request only reformats source and test files with isort and black (import ordering, line wrapping, whitespace). It does not change the behaviour or properties of Qrisp. It also states no rule that code must be formatted this way, so no requirement can be reconstructed. |
| [407](https://github.com/eclipse-qrisp/Qrisp/pull/407) | Eingabe nicht verwertbar | The material has only the title "E.C.", with no description, no comments and no diff text. There is nothing to derive a requirement from. |

