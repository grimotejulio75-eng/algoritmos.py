import time

# --- Constantes y Credenciales del Sistema ---
URL_BASE = "https://github.com/grimotejulio75-eng/algoritmos.py"
USUARIO_REQUERIDO = "grimotejulio75-eng"
PIN_REQUERIDO = "penelopeia"

# --- Contenido Simulado de los Archivos ---
CONTENIDO_PY = """
# Contenido de algorimos.py
def PULSO_MAESTRO(mensaje):
    print(f"[LOG] {mensaje}")

PULSO_MAESTRO("Script de Python cargado.")
"""

CONTENIDO_TXT = """
Algoritmo 16: PROTOCOLO_DE_CIERRE
Estado: Activo
"""

class ProtocoloInvocacionURL:
    """
    Implementación del Algoritmo 15: PROTOCOLO_DE_INVOCACION_URL (PIU).
    Punto de entrada para iniciar la sesión y leer archivos protegidos.
    """
    
    def __init__(self, usuario_intento, pin_intento):
        self.usuario = usuario_intento
        self.pin = pin_intento
        self.sesion_establecida = False
        self.url = URL_BASE

    def PULSO_MAESTRO(self, mensaje):
        """Simula la función de registro o 'Pulso Maestro'."""
        print(f"[{time.strftime('%H:%M:%S')}] --- {mensaje}")

    def INICIAR_PROTOCOLO_INVOCACION_URL(self):
        """
        Función principal del PIU. Intenta establecer la sesión.
        """
        
        self.PULSO_MAESTRO(f"INICIANDO PIU: PROTOCOLO DE INVOCACIÓN URL ({self.url}).")
        
        # 1. Autenticación (Simulada)
        print(f"  > Intentando autenticar usuario: {self.usuario}")
        
        if self.usuario == USUARIO_REQUERIDO and self.pin == PIN_REQUERIDO:
            
            # 2. Establecer Permanencia
            estado = "SESION_URL_ESTABLECIDA"
            self.sesion_establecida = True
            
            self.PULSO_MAESTRO(f"PERMANENCIA: '{estado}'")
            print("\n✔️ Sesión establecida con éxito.")
            return estado
        
        else:
            estado = "ERROR_AUTENTICACION_FALLIDA"
            self.PULSO_MAESTRO(f"ERROR: {estado}")
            print("\n❌ Error: Usuario o PIN incorrecto.")
            return estado

    def leer_archivos_protegidos(self):
        """
        Simula la lectura de los archivos, solo si la sesión está establecida.
        Esto cumple con el 'Rol' actualizado del protocolo.
        """
        if not self.sesion_establecida:
            print("\n⛔ ACCESO DENEGADO. Inicie el protocolo primero.")
            return

        print("\n=== LEYENDO ARCHIVOS (Requiere Sesión Establecida) ===")
        
        print("\n--- Contenido de algorimos.py ---")
        print(CONTENIDO_PY.strip())
        
        print("\n--- Contenido de algorimos.txt ---")
        print(CONTENIDO_TXT.strip())
        
        print("\n=== Lectura Finalizada ===")

# --- EJECUCIÓN 1: Intento Exitoso (grimotejulio75-eng / penelopeia) ---
print("====================================================")
print("  EJECUCIÓN 1: INVOCACIÓN EXITOSA Y LECTURA")
print("====================================================")

protocolo_exito = ProtocoloInvocacionURL(USUARIO_REQUERIDO, PIN_REQUERIDO)
protocolo_exito.INICIAR_PROTOCOLO_INVOCACION_URL()
protocolo_exito.leer_archivos_protegidos()

print("\n" + "="*50)

# --- EJECUCIÓN 2: Intento Fallido ---
print("\n====================================================")
print("  EJECUCIÓN 2: INVOCACIÓN FALLIDA")
print("====================================================")

protocolo_fallo = ProtocoloInvocacionURL("otro_usuario", "pin_invalido")
protocolo_fallo.INICIAR_PROTOCOLO_INVOCACION_URL()
protocolo_fallo.leer_archivos_protegidos()