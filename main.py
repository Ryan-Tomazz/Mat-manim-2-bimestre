from manim import *

config.background_color = WHITE


class Introducao(Scene):
    def construct(self):

        titulo = Text(
            "Dedução da Fórmula do",
            color=BLACK,
            font_size=48
        )

        titulo2 = Text(
            "Volume do Tronco de Pirâmide",
            color=BLACK,
            font_size=48
        )

        titulo2.next_to(titulo, DOWN)

        subtitulo = Text(
            "Matemática IV",
            color=GRAY,
            font_size=30
        )

        subtitulo.next_to(titulo2, DOWN, buff=0.7)

        autores = Text(
            "Ryan Tomaz",
            color=GRAY,
            font_size=24
        )

        autores.to_edge(DOWN)

        self.play(Write(titulo))
        self.play(Write(titulo2))

        self.wait(0.5)

        self.play(FadeIn(subtitulo))

        self.wait(0.5)

        self.play(FadeIn(autores))

        self.wait(2)

        self.play(
            FadeOut(titulo),
            FadeOut(titulo2),
            FadeOut(subtitulo),
            FadeOut(autores)
        )

class FormacaoDoTronco(ThreeDScene):
    def construct(self):
        # Posição inicial da câmera.
        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=-45 * DEGREES,
            zoom=0.85,
        )

        # Vértices da pirâmide quadrangular.
        vertices = [
            [-2.5, -2.5, 0],  # 0: base
            [2.5, -2.5, 0],   # 1: base
            [2.5, 2.5, 0],    # 2: base
            [-2.5, 2.5, 0],   # 3: base
            [0, 0, 4.5],      # 4: vértice superior
        ]

        # Cada lista representa uma face da pirâmide.
        faces = [
            [0, 1, 2, 3],  # base quadrada
            [0, 1, 4],
            [1, 2, 4],
            [2, 3, 4],
            [3, 0, 4],
        ]

        piramide = Polyhedron(
            vertex_coords=vertices,
            faces_list=faces,
            faces_config={
                "fill_color": BLUE_D,
                "fill_opacity": 0.25,
                "stroke_color": BLUE_E,
                "stroke_width": 2,
            },
            graph_config={
                "vertex_config": {
                    "radius": 0.045,
                    "color": BLUE_E,
                },
                "edge_config": {
                    "stroke_color": BLUE_E,
                    "stroke_width": 3,
                },
            },
        )

        # Plano paralelo à base, situado no interior da pirâmide.
        plano_de_corte = Square(
            side_length=2.8,
            fill_color=YELLOW,
            fill_opacity=0.45,
            stroke_color=ORANGE,
            stroke_width=3,
        )

        # Um Square nasce no plano XY. Por isso, só precisamos elevá-lo.
        plano_de_corte.shift(2.0 * OUT)

        titulo = Text(
            "Formação de um tronco de pirâmide",
            color=BLACK,
            font_size=34,
        ).to_edge(UP)

        explicacao = Text(
            "Um plano paralelo à base corta a pirâmide.",
            color=BLACK,
            font_size=28,
        ).to_edge(DOWN)

        # Os textos permanecem parados na tela enquanto a câmera gira.
        self.add_fixed_in_frame_mobjects(titulo, explicacao)

        self.play(Write(titulo))
        self.play(Create(piramide), run_time=2.5)
        self.wait(1)

        # Pequena rotação para evidenciar que a figura é tridimensional.
        self.begin_ambient_camera_rotation(rate=0.12)
        self.wait(2)
        self.stop_ambient_camera_rotation()

        self.play(
            FadeIn(plano_de_corte, shift=0.4 * OUT),
            run_time=1.5,
        )

        self.play(Write(explicacao))
        self.wait(3)

        # Destaca visualmente a região do corte.
        self.play(
            plano_de_corte.animate.set_fill(opacity=0.7).scale(1.06),
            run_time=0.7,
        )

        self.play(
            plano_de_corte.animate.set_fill(opacity=0.45).scale(1 / 1.06),
            run_time=0.7,
        )

        self.wait(2)

        self.play(
            FadeOut(piramide),
            FadeOut(plano_de_corte),
            FadeOut(titulo),
            FadeOut(explicacao),
        )

class SeparacaoDoTronco(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=-45 * DEGREES,
            zoom=0.8,
        )

        # Medidas usadas na construção
        altura_total = 4.5
        altura_corte = 2.0
        metade_base_maior = 2.5

        # Pela semelhança, o quadrado do corte diminui
        # proporcionalmente à distância até o vértice.
        metade_base_menor = metade_base_maior * (
            1 - altura_corte / altura_total
        )

        # -----------------------------
        # Tronco de pirâmide
        # -----------------------------

        vertices_tronco = [
            # Base maior: z = 0
            [-metade_base_maior, -metade_base_maior, 0],
            [metade_base_maior, -metade_base_maior, 0],
            [metade_base_maior, metade_base_maior, 0],
            [-metade_base_maior, metade_base_maior, 0],

            # Base menor: z = altura_corte
            [-metade_base_menor, -metade_base_menor, altura_corte],
            [metade_base_menor, -metade_base_menor, altura_corte],
            [metade_base_menor, metade_base_menor, altura_corte],
            [-metade_base_menor, metade_base_menor, altura_corte],
        ]

        faces_tronco = [
            [0, 1, 2, 3],  # base maior
            [4, 5, 6, 7],  # base menor
            [0, 1, 5, 4],
            [1, 2, 6, 5],
            [2, 3, 7, 6],
            [3, 0, 4, 7],
        ]

        tronco = Polyhedron(
            vertex_coords=vertices_tronco,
            faces_list=faces_tronco,
            faces_config={
                "fill_color": BLUE_D,
                "fill_opacity": 0.35,
                "stroke_color": BLUE_E,
                "stroke_width": 2,
            },
            graph_config={
                "vertex_config": {
                    "radius": 0.04,
                    "color": BLUE_E,
                },
                "edge_config": {
                    "stroke_color": BLUE_E,
                    "stroke_width": 3,
                },
            },
        )

        # -----------------------------
        # Pirâmide menor
        # -----------------------------

        vertices_piramide_menor = [
            [-metade_base_menor, -metade_base_menor, altura_corte],
            [metade_base_menor, -metade_base_menor, altura_corte],
            [metade_base_menor, metade_base_menor, altura_corte],
            [-metade_base_menor, metade_base_menor, altura_corte],
            [0, 0, altura_total],
        ]

        faces_piramide_menor = [
            [0, 1, 2, 3],
            [0, 1, 4],
            [1, 2, 4],
            [2, 3, 4],
            [3, 0, 4],
        ]

        piramide_menor = Polyhedron(
            vertex_coords=vertices_piramide_menor,
            faces_list=faces_piramide_menor,
            faces_config={
                "fill_color": ORANGE,
                "fill_opacity": 0.45,
                "stroke_color": ORANGE,
                "stroke_width": 2,
            },
            graph_config={
                "vertex_config": {
                    "radius": 0.04,
                    "color": ORANGE,
                },
                "edge_config": {
                    "stroke_color": ORANGE,
                    "stroke_width": 3,
                },
            },
        )

        titulo = Text(
            "Separação da pirâmide",
            color=BLACK,
            font_size=34,
        ).to_edge(UP)

        texto_inicial = Text(
            "O corte divide a pirâmide em duas partes.",
            color=BLACK,
            font_size=27,
        ).to_edge(DOWN)

        texto_tronco = Text(
            "Tronco de pirâmide",
            color=BLUE_E,
            font_size=27,
        ).to_edge(DOWN)

        texto_superior = Text(
            "Pirâmide menor",
            color=ORANGE,
            font_size=27,
        ).to_edge(DOWN)

        ideia = VGroup(
            Text(
                "Volume do tronco",
                color=BLUE_E,
                font_size=29,
            ),
            Text(
                "=",
                color=BLACK,
                font_size=32,
            ),
            Text(
                "volume da pirâmide maior",
                color=BLACK,
                font_size=29,
            ),
            Text(
                "−",
                color=BLACK,
                font_size=32,
            ),
            Text(
                "volume da pirâmide menor",
                color=ORANGE,
                font_size=29,
            ),
        ).arrange(RIGHT, buff=0.18)

        ideia.scale_to_fit_width(12)
        ideia.to_edge(DOWN)

        self.add_fixed_in_frame_mobjects(
            titulo,
            texto_inicial,
        )

        self.play(Write(titulo))

        # As duas peças aparecem juntas, formando a pirâmide completa.
        self.play(
            Create(tronco),
            Create(piramide_menor),
            run_time=2.5,
        )

        self.play(Write(texto_inicial))
        self.wait(2)

        # Remove o primeiro texto.
        self.play(FadeOut(texto_inicial))
        self.remove_fixed_in_frame_mobjects(texto_inicial)

        # A pirâmide superior é deslocada para cima,
        # mostrando visualmente a separação.
        self.play(
            piramide_menor.animate.shift(1.5 * OUT),
            run_time=2,
        )

        self.wait(1)

        self.add_fixed_in_frame_mobjects(texto_superior)
        self.play(Write(texto_superior))
        self.wait(1.5)

        self.play(FadeOut(texto_superior))
        self.remove_fixed_in_frame_mobjects(texto_superior)

        self.add_fixed_in_frame_mobjects(texto_tronco)
        self.play(Write(texto_tronco))

        # Destaca o tronco.
        self.play(
            tronco.animate.set_opacity(0.65),
            run_time=0.8,
        )

        self.play(
            tronco.animate.set_opacity(0.35),
            run_time=0.8,
        )

        self.wait(1)

        self.play(FadeOut(texto_tronco))
        self.remove_fixed_in_frame_mobjects(texto_tronco)

        # Retorna a parte superior à posição original.
        self.play(
            piramide_menor.animate.shift(1.5 * IN),
            run_time=1.5,
        )

        self.wait(1)

        # Apresenta a ideia central da dedução.
        self.add_fixed_in_frame_mobjects(ideia)

        self.play(
            LaggedStart(
                *[Write(parte) for parte in ideia],
                lag_ratio=0.25,
            ),
            run_time=4,
        )

        self.wait(3)

        # Pequena rotação para mostrar o sólido completo.
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(3)
        self.stop_ambient_camera_rotation()

        self.play(
            FadeOut(tronco),
            FadeOut(piramide_menor),
            FadeOut(titulo),
            FadeOut(ideia),
        )

class IdentificacaoDasMedidas(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=-45 * DEGREES,
            zoom=0.82,
            frame_center=1.5 * LEFT,
        )

        # -----------------------------
        # Medidas geométricas
        # -----------------------------

        altura_total = 4.5
        altura_tronco = 2.0
        altura_menor = altura_total - altura_tronco

        metade_base_maior = 2.5
        metade_base_menor = (
            metade_base_maior * altura_menor / altura_total
        )

        # -----------------------------
        # Tronco de pirâmide
        # -----------------------------

        vertices_tronco = [
            [-metade_base_maior, -metade_base_maior, 0],
            [metade_base_maior, -metade_base_maior, 0],
            [metade_base_maior, metade_base_maior, 0],
            [-metade_base_maior, metade_base_maior, 0],

            [-metade_base_menor, -metade_base_menor, altura_tronco],
            [metade_base_menor, -metade_base_menor, altura_tronco],
            [metade_base_menor, metade_base_menor, altura_tronco],
            [-metade_base_menor, metade_base_menor, altura_tronco],
        ]

        faces_tronco = [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [0, 1, 5, 4],
            [1, 2, 6, 5],
            [2, 3, 7, 6],
            [3, 0, 4, 7],
        ]

        tronco = Polyhedron(
            vertex_coords=vertices_tronco,
            faces_list=faces_tronco,
            faces_config={
                "fill_color": BLUE_D,
                "fill_opacity": 0.28,
                "stroke_color": BLUE_E,
                "stroke_width": 2,
            },
            graph_config={
                "vertex_config": {
                    "radius": 0.035,
                    "color": BLUE_E,
                },
                "edge_config": {
                    "stroke_color": BLUE_E,
                    "stroke_width": 3,
                },
            },
        )

        # -----------------------------
        # Pirâmide superior
        # -----------------------------

        vertices_superior = [
            [-metade_base_menor, -metade_base_menor, altura_tronco],
            [metade_base_menor, -metade_base_menor, altura_tronco],
            [metade_base_menor, metade_base_menor, altura_tronco],
            [-metade_base_menor, metade_base_menor, altura_tronco],
            [0, 0, altura_total],
        ]

        faces_superior = [
            [0, 1, 2, 3],
            [0, 1, 4],
            [1, 2, 4],
            [2, 3, 4],
            [3, 0, 4],
        ]

        piramide_superior = Polyhedron(
            vertex_coords=vertices_superior,
            faces_list=faces_superior,
            faces_config={
                "fill_color": ORANGE,
                "fill_opacity": 0.22,
                "stroke_color": ORANGE,
                "stroke_width": 2,
            },
            graph_config={
                "vertex_config": {
                    "radius": 0.035,
                    "color": ORANGE,
                },
                "edge_config": {
                    "stroke_color": ORANGE,
                    "stroke_width": 3,
                },
            },
        )

        # -----------------------------
        # Segmentos que representam
        # as alturas h, d e k
        # -----------------------------

        deslocamento_x = -3.15

        linha_h = Line3D(
            start=[deslocamento_x, 0, 0],
            end=[deslocamento_x, 0, altura_total],
            thickness=0.025,
            color=PURPLE,
        )

        linha_k = Line3D(
            start=[deslocamento_x - 0.18, 0, 0],
            end=[deslocamento_x - 0.18, 0, altura_tronco],
            thickness=0.035,
            color=RED,
        )

        linha_d = Line3D(
            start=[deslocamento_x - 0.18, 0, altura_tronco],
            end=[deslocamento_x - 0.18, 0, altura_total],
            thickness=0.035,
            color=ORANGE,
        )

        # Line3D é apropriado para segmentos inseridos em cenas 3D.
        # Ele é renderizado como um pequeno cilindro.
        # -----------------------------
        # Título e legenda fixa
        # -----------------------------

        titulo = Text(
            "Identificação das medidas",
            color=BLACK,
            font_size=34,
        ).to_edge(UP)

        item_B = MathTex(
            r"B",
            r"\;=\;",
            r"\text{área da base maior}",
            color=BLACK,
            font_size=34,
        )

        item_b = MathTex(
            r"b",
            r"\;=\;",
            r"\text{área da base menor}",
            color=BLACK,
            font_size=34,
        )

        item_h = MathTex(
            r"h",
            r"\;=\;",
            r"\text{altura da pirâmide maior}",
            color=BLACK,
            font_size=34,
        )

        item_d = MathTex(
            r"d",
            r"\;=\;",
            r"\text{altura da pirâmide menor}",
            color=BLACK,
            font_size=34,
        )

        item_k = MathTex(
            r"k",
            r"\;=\;",
            r"\text{altura do tronco}",
            color=BLACK,
            font_size=34,
        )

        item_B[0].set_color(BLUE_E)
        item_b[0].set_color(GREEN_D)
        item_h[0].set_color(PURPLE)
        item_d[0].set_color(ORANGE)
        item_k[0].set_color(RED)

        legenda = VGroup(
            item_B,
            item_b,
            item_h,
            item_d,
            item_k,
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.35,
        )

        legenda.scale_to_fit_width(5.4)
        legenda.to_edge(RIGHT, buff=0.45)
        legenda.shift(0.25 * UP)

        relacao = MathTex(
            r"k",
            r"=",
            r"h",
            r"-",
            r"d",
            font_size=54,
            color=BLACK,
        ).to_edge(DOWN)

        relacao[0].set_color(RED)
        relacao[2].set_color(PURPLE)
        relacao[4].set_color(ORANGE)

        # -----------------------------
        # Rótulos próximos da figura
        # Eles ficarão fixos na tela para
        # permanecerem legíveis.
        # -----------------------------

        rotulo_B = MathTex(
            r"B",
            color=BLUE_E,
            font_size=42,
        ).move_to([-3.2, -2.15, 0])

        rotulo_b = MathTex(
            r"b",
            color=GREEN_D,
            font_size=42,
        ).move_to([-2.35, 0.35, 0])

        rotulo_h = MathTex(
            r"h",
            color=PURPLE,
            font_size=42,
        ).move_to([-5.05, 0.25, 0])

        rotulo_k = MathTex(
            r"k",
            color=RED,
            font_size=42,
        ).move_to([-4.55, -0.85, 0])

        rotulo_d = MathTex(
            r"d",
            color=ORANGE,
            font_size=42,
        ).move_to([-4.55, 1.15, 0])

        objetos_fixos = [
            titulo,
            legenda,
            relacao,
            rotulo_B,
            rotulo_b,
            rotulo_h,
            rotulo_k,
            rotulo_d,
        ]

        self.add_fixed_in_frame_mobjects(*objetos_fixos)

        # Os objetos são adicionados como fixos, mas ficam inicialmente
        # invisíveis para que possam ser animados depois.
        for objeto in objetos_fixos:
            objeto.set_opacity(0)

        # -----------------------------
        # Animação
        # -----------------------------

        self.play(
            titulo.animate.set_opacity(1),
            run_time=0.8,
        )

        self.play(
            Create(tronco),
            Create(piramide_superior),
            run_time=2.5,
        )

        self.wait(1)

        # Base maior: B
        self.play(
            FadeIn(item_B),
            FadeIn(rotulo_B),
            tronco.animate.set_fill(BLUE_D, opacity=0.42),
            run_time=1.2,
        )

        self.wait(1)

        # Base menor: b
        self.play(
            FadeIn(item_b),
            FadeIn(rotulo_b),
            run_time=1.2,
        )

        self.wait(1)

        # Altura total: h
        self.play(
            Create(linha_h),
            FadeIn(item_h),
            FadeIn(rotulo_h),
            run_time=1.4,
        )

        self.wait(1)

        # Altura da pirâmide menor: d
        self.play(
            Create(linha_d),
            FadeIn(item_d),
            FadeIn(rotulo_d),
            run_time=1.4,
        )

        self.wait(1)

        # Altura do tronco: k
        self.play(
            Create(linha_k),
            FadeIn(item_k),
            FadeIn(rotulo_k),
            run_time=1.4,
        )

        self.wait(2)

        # Relação entre as alturas
        self.play(
            relacao.animate.set_opacity(1),
            run_time=0.8,
        )

        self.play(
            Circumscribe(
                relacao,
                color=RED,
                buff=0.18,
            ),
            run_time=1.5,
        )

        self.wait(3)

        self.play(
            FadeOut(tronco),
            FadeOut(piramide_superior),
            FadeOut(linha_h),
            FadeOut(linha_d),
            FadeOut(linha_k),
            *[
                objeto.animate.set_opacity(0)
                for objeto in objetos_fixos
            ],
            run_time=1.5,
        )