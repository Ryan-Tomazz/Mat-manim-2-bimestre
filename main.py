from manim import *

config.background_color = WHITE


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def criar_piramide_completa(
    metade_base=2.5,
    altura=4.5,
    cor=BLUE_D,
    opacidade=0.25,
):
    vertices = [
        [-metade_base, -metade_base, 0],
        [metade_base, -metade_base, 0],
        [metade_base, metade_base, 0],
        [-metade_base, metade_base, 0],
        [0, 0, altura],
    ]

    faces = [
        [0, 1, 2, 3],
        [0, 1, 4],
        [1, 2, 4],
        [2, 3, 4],
        [3, 0, 4],
    ]

    return Polyhedron(
        vertex_coords=vertices,
        faces_list=faces,
        faces_config={
            "fill_color": cor,
            "fill_opacity": opacidade,
            "stroke_color": cor,
            "stroke_width": 2,
        },
        graph_config={
            "vertex_config": {
                "radius": 0.04,
                "color": cor,
            },
            "edge_config": {
                "stroke_color": cor,
                "stroke_width": 3,
            },
        },
    )


def criar_tronco_e_piramide_menor(
    metade_base_maior=2.5,
    altura_total=4.5,
    altura_tronco=2.0,
):
    altura_menor = altura_total - altura_tronco
    metade_base_menor = metade_base_maior * altura_menor / altura_total

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
            "fill_opacity": 0.32,
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

    vertices_menor = [
        [-metade_base_menor, -metade_base_menor, altura_tronco],
        [metade_base_menor, -metade_base_menor, altura_tronco],
        [metade_base_menor, metade_base_menor, altura_tronco],
        [-metade_base_menor, metade_base_menor, altura_tronco],
        [0, 0, altura_total],
    ]

    faces_menor = [
        [0, 1, 2, 3],
        [0, 1, 4],
        [1, 2, 4],
        [2, 3, 4],
        [3, 0, 4],
    ]

    piramide_menor = Polyhedron(
        vertex_coords=vertices_menor,
        faces_list=faces_menor,
        faces_config={
            "fill_color": ORANGE,
            "fill_opacity": 0.40,
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

    return tronco, piramide_menor, metade_base_menor


# ============================================================
# CENA 1 — INTRODUÇÃO
# ============================================================

class Introducao(Scene):
    def construct(self):
        titulo = VGroup(
            Text(
                "Dedução da Fórmula do",
                color=BLACK,
                font_size=48,
            ),
            Text(
                "Volume do Tronco de Pirâmide",
                color=BLACK,
                font_size=48,
            ),
        ).arrange(DOWN, buff=0.2)

        subtitulo = Text(
            "Matemática IV",
            color=GRAY_D,
            font_size=30,
        ).next_to(titulo, DOWN, buff=0.7)

        autor = Text(
            "Ryan Tomaz",
            color=GRAY_D,
            font_size=24,
        ).to_edge(DOWN)

        self.play(Write(titulo), run_time=2)
        self.play(FadeIn(subtitulo, shift=0.2 * UP))
        self.play(FadeIn(autor))
        self.wait(2)
        self.play(FadeOut(VGroup(titulo, subtitulo, autor)))


# ============================================================
# CENA 2 — FORMAÇÃO DO TRONCO
# ============================================================

class FormacaoDoTronco(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=-45 * DEGREES,
            zoom=0.85,
        )

        piramide = criar_piramide_completa()

        plano_de_corte = Square(
            side_length=2.8,
            fill_color=YELLOW,
            fill_opacity=0.45,
            stroke_color=ORANGE,
            stroke_width=3,
        ).shift(2.0 * OUT)

        titulo = Text(
            "Formação de um tronco de pirâmide",
            color=BLACK,
            font_size=34,
        ).to_edge(UP)

        explicacao = Text(
            "Um plano paralelo à base corta a pirâmide.",
            color=BLACK,
            font_size=27,
        ).to_edge(DOWN)

        self.add_fixed_in_frame_mobjects(titulo, explicacao)
        explicacao.set_opacity(0)

        self.play(Write(titulo))
        self.play(Create(piramide), run_time=2.5)

        self.begin_ambient_camera_rotation(rate=0.10)
        self.wait(2)
        self.stop_ambient_camera_rotation()

        self.play(FadeIn(plano_de_corte, shift=0.3 * OUT))
        self.play(explicacao.animate.set_opacity(1))
        self.wait(2)

        self.play(
            plano_de_corte.animate.set_fill(opacity=0.75).scale(1.06),
            run_time=0.7,
        )
        self.play(
            plano_de_corte.animate.set_fill(opacity=0.45).scale(1 / 1.06),
            run_time=0.7,
        )
        self.wait(1)

        self.play(
            FadeOut(piramide),
            FadeOut(plano_de_corte),
            FadeOut(titulo),
            FadeOut(explicacao),
        )


# ============================================================
# CENA 3 — SEPARAÇÃO DAS DUAS PARTES
# ============================================================

class SeparacaoDoTronco(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=-45 * DEGREES,
            zoom=0.82,
        )

        tronco, piramide_menor, _ = criar_tronco_e_piramide_menor()

        titulo = Text(
            "Separação da pirâmide",
            color=BLACK,
            font_size=34,
        ).to_edge(UP)

        explicacao = Text(
            "O corte divide a pirâmide em duas partes.",
            color=BLACK,
            font_size=27,
        ).to_edge(DOWN)

        formula_verbal = VGroup(
            Text("Volume do tronco", color=BLUE_E, font_size=26),
            Text("=", color=BLACK, font_size=30),
            Text("volume da pirâmide maior", color=BLACK, font_size=26),
            Text("−", color=BLACK, font_size=30),
            Text("volume da pirâmide menor", color=ORANGE, font_size=26),
        ).arrange(RIGHT, buff=0.16)
        formula_verbal.scale_to_fit_width(12.5)
        formula_verbal.to_edge(DOWN)

        self.add_fixed_in_frame_mobjects(titulo, explicacao, formula_verbal)
        explicacao.set_opacity(0)
        formula_verbal.set_opacity(0)

        self.play(Write(titulo))
        self.play(Create(tronco), Create(piramide_menor), run_time=2.5)
        self.play(explicacao.animate.set_opacity(1))
        self.wait(1.5)

        self.play(explicacao.animate.set_opacity(0))
        self.play(piramide_menor.animate.shift(1.5 * OUT), run_time=1.8)
        self.wait(1)

        destaque_superior = Text(
            "Pirâmide menor",
            color=ORANGE,
            font_size=28,
        ).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(destaque_superior)
        self.play(Write(destaque_superior))
        self.wait(1)
        self.play(FadeOut(destaque_superior))

        destaque_tronco = Text(
            "Tronco de pirâmide",
            color=BLUE_E,
            font_size=28,
        ).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(destaque_tronco)
        self.play(Write(destaque_tronco))
        self.play(tronco.animate.set_opacity(0.65), run_time=0.6)
        self.play(tronco.animate.set_opacity(0.32), run_time=0.6)
        self.wait(1)
        self.play(FadeOut(destaque_tronco))

        self.play(piramide_menor.animate.shift(1.5 * IN), run_time=1.5)
        self.play(formula_verbal.animate.set_opacity(1), run_time=1.5)
        self.wait(3)

        self.play(
            FadeOut(tronco),
            FadeOut(piramide_menor),
            FadeOut(titulo),
            FadeOut(formula_verbal),
        )


# ============================================================
# CENA 4 — IDENTIFICAÇÃO DAS MEDIDAS
# ============================================================

class IdentificacaoDasMedidas(Scene):
    def construct(self):
        titulo = Text(
            "Identificação das medidas",
            color=BLACK,
            font_size=36,
        ).to_edge(UP)

        # Figura 2D limpa e estável para explicar as variáveis.
        base_maior_esq = np.array([-5.2, -2.3, 0])
        base_maior_dir = np.array([-0.8, -2.3, 0])
        base_menor_esq = np.array([-4.2, 0.15, 0])
        base_menor_dir = np.array([-1.8, 0.15, 0])
        vertice = np.array([-3.0, 2.5, 0])

        contorno = VGroup(
            Line(base_maior_esq, base_maior_dir, color=BLUE_E, stroke_width=4),
            Line(base_maior_esq, vertice, color=BLACK, stroke_width=3),
            Line(base_maior_dir, vertice, color=BLACK, stroke_width=3),
            Line(base_menor_esq, base_menor_dir, color=GREEN_D, stroke_width=4),
        )

        # Linhas das alturas, desenhadas ao lado da figura.
        x_alturas = -5.75
        linha_h = Line(
            [x_alturas, -2.3, 0],
            [x_alturas, 2.5, 0],
            color=PURPLE,
            stroke_width=5,
        )
        linha_k = Line(
            [x_alturas - 0.25, -2.3, 0],
            [x_alturas - 0.25, 0.15, 0],
            color=RED,
            stroke_width=6,
        )
        linha_d = Line(
            [x_alturas - 0.25, 0.15, 0],
            [x_alturas - 0.25, 2.5, 0],
            color=ORANGE,
            stroke_width=6,
        )

        rotulo_B = MathTex("B", color=BLUE_E, font_size=44).next_to(
            contorno[0], DOWN, buff=0.2
        )
        rotulo_b = MathTex("b", color=GREEN_D, font_size=44).next_to(
            contorno[3], UP, buff=0.15
        )
        rotulo_h = MathTex("h", color=PURPLE, font_size=42).next_to(
            linha_h, LEFT, buff=0.18
        )
        rotulo_k = MathTex("k", color=RED, font_size=42).next_to(
            linha_k, LEFT, buff=0.18
        )
        rotulo_d = MathTex("d", color=ORANGE, font_size=42).next_to(
            linha_d, LEFT, buff=0.18
        )

        item_B = VGroup(
            MathTex("B", color=BLUE_E, font_size=38),
            Text("= área da base maior", color=BLACK, font_size=27),
        ).arrange(RIGHT, buff=0.18)

        item_b = VGroup(
            MathTex("b", color=GREEN_D, font_size=38),
            Text("= área da base menor", color=BLACK, font_size=27),
        ).arrange(RIGHT, buff=0.18)

        item_h = VGroup(
            MathTex("h", color=PURPLE, font_size=38),
            Text("= altura da pirâmide maior", color=BLACK, font_size=27),
        ).arrange(RIGHT, buff=0.18)

        item_d = VGroup(
            MathTex("d", color=ORANGE, font_size=38),
            Text("= altura da pirâmide menor", color=BLACK, font_size=27),
        ).arrange(RIGHT, buff=0.18)

        item_k = VGroup(
            MathTex("k", color=RED, font_size=38),
            Text("= altura do tronco", color=BLACK, font_size=27),
        ).arrange(RIGHT, buff=0.18)

        legenda = VGroup(item_B, item_b, item_h, item_d, item_k).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.38,
        )
        legenda.to_edge(RIGHT, buff=0.55)
        legenda.shift(0.15 * UP)

        relacao = MathTex(
            "k", "=", "h", "-", "d",
            color=BLACK,
            font_size=58,
        ).to_edge(DOWN)
        relacao[0].set_color(RED)
        relacao[2].set_color(PURPLE)
        relacao[4].set_color(ORANGE)

        self.play(Write(titulo))
        self.play(Create(contorno), run_time=2)

        self.play(Write(rotulo_B), FadeIn(item_B, shift=0.2 * LEFT))
        self.wait(0.6)

        self.play(Write(rotulo_b), FadeIn(item_b, shift=0.2 * LEFT))
        self.wait(0.6)

        self.play(Create(linha_h), Write(rotulo_h), FadeIn(item_h, shift=0.2 * LEFT))
        self.wait(0.6)

        self.play(Create(linha_d), Write(rotulo_d), FadeIn(item_d, shift=0.2 * LEFT))
        self.wait(0.6)

        self.play(Create(linha_k), Write(rotulo_k), FadeIn(item_k, shift=0.2 * LEFT))
        self.wait(1.5)

        self.play(Write(relacao), run_time=1.2)
        self.play(Circumscribe(relacao, color=RED, buff=0.18))
        self.wait(3)

        self.play(
            FadeOut(
                VGroup(
                    titulo,
                    contorno,
                    linha_h,
                    linha_k,
                    linha_d,
                    rotulo_B,
                    rotulo_b,
                    rotulo_h,
                    rotulo_k,
                    rotulo_d,
                    legenda,
                    relacao,
                )
            )
        )


# ============================================================
# CENA DE TESTE DO LATEX
# ============================================================

class TesteLatex(Scene):
    def construct(self):
        formula = MathTex(
            r"V=\frac{1}{3}Bh",
            font_size=64,
            color=BLACK,
        )
        self.play(Write(formula))
        self.wait(2)


# ============================================================
# CENA 5 — SEMELHANÇA ENTRE AS PIRÂMIDES
# ============================================================

class SemelhancaDasPiramides(Scene):
    def construct(self):
        titulo = Text(
            "Semelhança entre as pirâmides",
            color=BLACK,
            font_size=36,
        ).to_edge(UP)

        # Figura 2D da pirâmide maior e da pirâmide menor.
        vertice = np.array([-3.5, 2.2, 0])
        base_esquerda = np.array([-6.0, -2.3, 0])
        base_direita = np.array([-1.0, -2.3, 0])

        lado_esquerdo = Line(vertice, base_esquerda, color=BLUE_E, stroke_width=4)
        lado_direito = Line(vertice, base_direita, color=BLUE_E, stroke_width=4)
        base_maior = Line(base_esquerda, base_direita, color=BLUE_E, stroke_width=5)

        proporcao_corte = 0.55
        corte_esquerda = interpolate(vertice, base_esquerda, proporcao_corte)
        corte_direita = interpolate(vertice, base_direita, proporcao_corte)
        base_menor = Line(corte_esquerda, corte_direita, color=GREEN_D, stroke_width=5)

        piramide_menor = Polygon(
            vertice,
            corte_esquerda,
            corte_direita,
            color=ORANGE,
            stroke_width=3,
            fill_color=ORANGE,
            fill_opacity=0.16,
        )

        pe_altura = np.array([-3.5, -2.3, 0])
        pe_corte = np.array([-3.5, corte_esquerda[1], 0])

        altura_h = DashedLine(
            vertice,
            pe_altura,
            color=PURPLE,
            dash_length=0.12,
        )
        altura_d = Line(
            vertice,
            pe_corte,
            color=ORANGE,
            stroke_width=6,
        )

        rotulo_h = MathTex("h", color=PURPLE, font_size=42).next_to(
            altura_h, LEFT, buff=0.15
        )
        rotulo_d = MathTex("d", color=ORANGE, font_size=42).next_to(
            altura_d, RIGHT, buff=0.15
        )
        rotulo_B = MathTex("B", color=BLUE_E, font_size=46).next_to(
            base_maior, DOWN, buff=0.18
        )
        rotulo_b = MathTex("b", color=GREEN_D, font_size=46).next_to(
            base_menor, DOWN, buff=0.08
        )

        explicacao = Text(
            "O plano de corte é paralelo à base.",
            color=BLACK,
            font_size=26,
        ).move_to([3.1, 2.05, 0])

        conclusao = Text(
            "Logo, as duas pirâmides são semelhantes.",
            color=BLACK,
            font_size=24,
        ).next_to(explicacao, DOWN, buff=0.35)

        razao_linear = MathTex(
            r"\frac{\text{medida linear menor}}{\text{medida linear maior}}",
            r"=",
            r"\frac{d}{h}",
            color=BLACK,
            font_size=34,
        ).move_to([3.1, 0.75, 0])
        razao_linear[2].set_color(ORANGE)

        observacao_areas = Text(
            "A razão entre áreas é o quadrado\n"
            "da razão entre medidas lineares.",
            color=BLACK,
            font_size=23,
            line_spacing=0.9,
        ).move_to([3.1, -0.25, 0])

        razao_areas = MathTex(
            r"\frac{b}{B}",
            r"=",
            r"\left(\frac{d}{h}\right)^2",
            color=BLACK,
            font_size=50,
        ).move_to([3.1, -1.25, 0])
        razao_areas[0].set_color(GREEN_D)
        razao_areas[2].set_color(ORANGE)

        raiz = MathTex(
            r"\sqrt{\frac{b}{B}}",
            r"=",
            r"\frac{d}{h}",
            color=BLACK,
            font_size=50,
        ).move_to([3.1, -1.25, 0])
        raiz[0].set_color(GREEN_D)
        raiz[2].set_color(ORANGE)

        resultado = MathTex(
            r"\frac{\sqrt{b}}{\sqrt{B}}",
            r"=",
            r"\frac{d}{h}",
            color=BLACK,
            font_size=54,
        ).move_to([3.1, -1.25, 0])
        resultado[0].set_color(GREEN_D)
        resultado[2].set_color(ORANGE)

        figura = VGroup(
            lado_esquerdo,
            lado_direito,
            base_maior,
            base_menor,
            piramide_menor,
            altura_h,
            altura_d,
            rotulo_h,
            rotulo_d,
            rotulo_B,
            rotulo_b,
        )

        self.play(Write(titulo))
        self.play(
            Create(lado_esquerdo),
            Create(lado_direito),
            Create(base_maior),
            run_time=1.8,
        )
        self.play(Create(base_menor), Write(rotulo_b), Write(rotulo_B), run_time=1.2)
        self.play(FadeIn(piramide_menor), run_time=1)
        self.play(Write(explicacao))
        self.play(
            Indicate(base_menor, color=GREEN_D, scale_factor=1.08),
            Indicate(base_maior, color=BLUE_E, scale_factor=1.04),
        )
        self.play(Write(conclusao))
        self.play(Create(altura_h), Write(rotulo_h))
        self.play(Create(altura_d), Write(rotulo_d))
        self.play(Write(razao_linear), run_time=1.7)
        self.wait(1)
        self.play(FadeOut(razao_linear), FadeIn(observacao_areas))
        self.play(Write(razao_areas), run_time=1.7)
        self.play(Circumscribe(razao_areas, color=YELLOW_D, buff=0.16))
        self.wait(1)
        self.play(
            FadeOut(observacao_areas),
            TransformMatchingTex(razao_areas, raiz),
            run_time=1.4,
        )
        self.wait(1)
        self.play(TransformMatchingTex(raiz, resultado), run_time=1.4)

        caixa = SurroundingRectangle(
            resultado,
            color=GREEN_D,
            buff=0.18,
            stroke_width=3,
        )
        self.play(Create(caixa))
        self.wait(3)

        self.play(
            FadeOut(titulo),
            FadeOut(figura),
            FadeOut(explicacao),
            FadeOut(conclusao),
            FadeOut(resultado),
            FadeOut(caixa),
        )

# ============================================================
# CENA 6 — DEDUÇÃO DAS ALTURAS
# ============================================================

class DeducaoDasAlturas(Scene):
    def construct(self):
        titulo = Text(
            "Determinando as alturas",
            color=BLACK,
            font_size=38,
        ).to_edge(UP)

        subtitulo = Text(
            "Usaremos a semelhança entre as pirâmides",
            color=GRAY_D,
            font_size=25,
        ).next_to(titulo, DOWN, buff=0.25)

        # Relação encontrada na cena anterior.
        relacao_semelhanca = MathTex(
            r"\frac{\sqrt{b}}{\sqrt{B}}",
            r"=",
            r"\frac{d}{h}",
            color=BLACK,
            font_size=54,
        )

        relacao_semelhanca[0].set_color(GREEN_D)
        relacao_semelhanca[2].set_color(ORANGE)

        # Relação entre as alturas.
        relacao_alturas = MathTex(
            r"h",
            r"=",
            r"d",
            r"+",
            r"k",
            color=BLACK,
            font_size=54,
        )

        relacao_alturas[0].set_color(PURPLE)
        relacao_alturas[2].set_color(ORANGE)
        relacao_alturas[4].set_color(RED)

        relacoes = VGroup(
            relacao_semelhanca,
            relacao_alturas,
        ).arrange(DOWN, buff=0.65)

        relacoes.shift(0.25 * UP)

        explicacao = Text(
            "Substituímos h por d + k",
            color=BLACK,
            font_size=27,
        ).to_edge(DOWN, buff=0.65)

        # Primeira substituição.
        passo_1 = MathTex(
            r"\frac{\sqrt{b}}{\sqrt{B}}",
            r"=",
            r"\frac{d}{d+k}",
            color=BLACK,
            font_size=58,
        )

        passo_1[0].set_color(GREEN_D)
        passo_1[2].set_color(ORANGE)

        # Multiplicação cruzada.
        passo_2 = MathTex(
            r"d\sqrt{B}",
            r"=",
            r"(d+k)\sqrt{b}",
            color=BLACK,
            font_size=58,
        )

        passo_2[0].set_color(ORANGE)
        passo_2[2].set_color(GREEN_D)

        # Aplicação da distributiva.
        passo_3 = MathTex(
            r"d\sqrt{B}",
            r"=",
            r"d\sqrt{b}",
            r"+",
            r"k\sqrt{b}",
            color=BLACK,
            font_size=56,
        )

        passo_3[0].set_color(ORANGE)
        passo_3[2].set_color(GREEN_D)
        passo_3[4].set_color(RED)

        # Termos com d no mesmo lado.
        passo_4 = MathTex(
            r"d\sqrt{B}",
            r"-",
            r"d\sqrt{b}",
            r"=",
            r"k\sqrt{b}",
            color=BLACK,
            font_size=56,
        )

        passo_4[0].set_color(ORANGE)
        passo_4[2].set_color(ORANGE)
        passo_4[4].set_color(RED)

        # Colocando d em evidência.
        passo_5 = MathTex(
            r"d",
            r"\left(\sqrt{B}-\sqrt{b}\right)",
            r"=",
            r"k\sqrt{b}",
            color=BLACK,
            font_size=56,
        )

        passo_5[0].set_color(ORANGE)
        passo_5[1].set_color(BLUE_E)
        passo_5[3].set_color(RED)

        # Isolando d.
        resultado_d = MathTex(
            r"d",
            r"=",
            r"\frac{k\sqrt{b}}{\sqrt{B}-\sqrt{b}}",
            color=BLACK,
            font_size=60,
        )

        resultado_d[0].set_color(ORANGE)
        resultado_d[2].set_color(RED)

        # ----------------------------------------------------
        # Animação
        # ----------------------------------------------------

        self.play(Write(titulo))
        self.play(FadeIn(subtitulo, shift=0.15 * UP))

        self.play(
            Write(relacao_semelhanca),
            run_time=1.5,
        )

        self.play(
            Write(relacao_alturas),
            run_time=1.4,
        )

        self.wait(1)

        self.play(
            Indicate(
                relacao_alturas,
                color=RED,
                scale_factor=1.08,
            )
        )

        self.play(Write(explicacao))

        self.wait(1)

        self.play(
            FadeOut(relacoes),
            FadeOut(explicacao),
        )

        self.play(
            Write(passo_1),
            run_time=1.6,
        )

        self.wait(1)

        self.play(
            TransformMatchingTex(
                passo_1,
                passo_2,
            ),
            run_time=1.5,
        )

        self.wait(0.8)

        self.play(
            TransformMatchingTex(
                passo_2,
                passo_3,
            ),
            run_time=1.5,
        )

        self.wait(0.8)

        self.play(
            TransformMatchingTex(
                passo_3,
                passo_4,
            ),
            run_time=1.5,
        )

        self.wait(0.8)

        self.play(
            TransformMatchingTex(
                passo_4,
                passo_5,
            ),
            run_time=1.5,
        )

        self.wait(0.8)

        self.play(
            TransformMatchingTex(
                passo_5,
                resultado_d,
            ),
            run_time=1.7,
        )

        caixa_d = SurroundingRectangle(
            resultado_d,
            color=ORANGE,
            buff=0.22,
            stroke_width=4,
        )

        texto_resultado = Text(
            "Altura da pirâmide menor",
            color=BLACK,
            font_size=26,
        ).next_to(caixa_d, DOWN, buff=0.35)

        self.play(Create(caixa_d))
        self.play(FadeIn(texto_resultado))

        self.wait(3)

        # ----------------------------------------------------
        # Determinação de h
        # ----------------------------------------------------

        self.play(
            FadeOut(resultado_d),
            FadeOut(caixa_d),
            FadeOut(texto_resultado),
        )

        etapa_h = Text(
            "Agora determinamos h",
            color=BLACK,
            font_size=32,
        ).shift(2.2 * UP)

        formula_h_1 = MathTex(
            r"h",
            r"=",
            r"d",
            r"+",
            r"k",
            color=BLACK,
            font_size=58,
        )

        formula_h_1[0].set_color(PURPLE)
        formula_h_1[2].set_color(ORANGE)
        formula_h_1[4].set_color(RED)

        formula_h_2 = MathTex(
            r"h",
            r"=",
            r"\frac{k\sqrt{b}}{\sqrt{B}-\sqrt{b}}",
            r"+",
            r"k",
            color=BLACK,
            font_size=53,
        )

        formula_h_2[0].set_color(PURPLE)
        formula_h_2[2].set_color(ORANGE)
        formula_h_2[4].set_color(RED)

        formula_h_3 = MathTex(
            r"h",
            r"=",
            r"\frac{k\sqrt{b}+k(\sqrt{B}-\sqrt{b})}"
            r"{\sqrt{B}-\sqrt{b}}",
            color=BLACK,
            font_size=48,
        )

        formula_h_3[0].set_color(PURPLE)
        formula_h_3[2].set_color(RED)

        formula_h_4 = MathTex(
            r"h",
            r"=",
            r"\frac{k\sqrt{B}}{\sqrt{B}-\sqrt{b}}",
            color=BLACK,
            font_size=60,
        )

        formula_h_4[0].set_color(PURPLE)
        formula_h_4[2].set_color(BLUE_E)

        self.play(Write(etapa_h))
        self.play(Write(formula_h_1))

        self.wait(1)

        self.play(
            TransformMatchingTex(
                formula_h_1,
                formula_h_2,
            ),
            run_time=1.5,
        )

        self.wait(0.8)

        self.play(
            TransformMatchingTex(
                formula_h_2,
                formula_h_3,
            ),
            run_time=1.7,
        )

        self.wait(0.8)

        self.play(
            TransformMatchingTex(
                formula_h_3,
                formula_h_4,
            ),
            run_time=1.7,
        )

        caixa_h = SurroundingRectangle(
            formula_h_4,
            color=PURPLE,
            buff=0.22,
            stroke_width=4,
        )

        texto_h = Text(
            "Altura da pirâmide maior",
            color=BLACK,
            font_size=26,
        ).next_to(caixa_h, DOWN, buff=0.35)

        self.play(Create(caixa_h))
        self.play(FadeIn(texto_h))

        self.wait(3)

        self.play(
            FadeOut(
                VGroup(
                    titulo,
                    subtitulo,
                    etapa_h,
                    formula_h_4,
                    caixa_h,
                    texto_h,
                )
            )
        )

# ============================================================
# CENA 7 — FÓRMULA DO VOLUME DO TRONCO
# ============================================================

class FormulaVolumeDoTronco(Scene):
    def construct(self):
        titulo = Text(
            "Volume do tronco de pirâmide",
            color=BLACK,
            font_size=38,
        ).to_edge(UP)

        subtitulo = Text(
            "Subtrairemos o volume da pirâmide menor"
            " do volume da pirâmide maior",
            color=GRAY_D,
            font_size=24,
        ).next_to(titulo, DOWN, buff=0.25)

        # ----------------------------------------------------
        # Ideia inicial
        # ----------------------------------------------------

        ideia = MathTex(
            r"V_{\text{tronco}}",
            r"=",
            r"V_{\text{maior}}",
            r"-",
            r"V_{\text{menor}}",
            color=BLACK,
            font_size=52,
        )

        ideia[0].set_color(BLUE_E)
        ideia[2].set_color(PURPLE)
        ideia[4].set_color(ORANGE)

        volumes = MathTex(
            r"V_{\text{tronco}}",
            r"=",
            r"\frac{1}{3}Bh",
            r"-",
            r"\frac{1}{3}bd",
            color=BLACK,
            font_size=54,
        )

        volumes[0].set_color(BLUE_E)
        volumes[2].set_color(PURPLE)
        volumes[4].set_color(ORANGE)

        # ----------------------------------------------------
        # Valores encontrados anteriormente
        # ----------------------------------------------------

        formula_h = MathTex(
            r"h",
            r"=",
            r"\frac{k\sqrt{B}}{\sqrt{B}-\sqrt{b}}",
            color=BLACK,
            font_size=43,
        )

        formula_h[0].set_color(PURPLE)
        formula_h[2].set_color(PURPLE)

        formula_d = MathTex(
            r"d",
            r"=",
            r"\frac{k\sqrt{b}}{\sqrt{B}-\sqrt{b}}",
            color=BLACK,
            font_size=43,
        )

        formula_d[0].set_color(ORANGE)
        formula_d[2].set_color(ORANGE)

        valores = VGroup(
            formula_h,
            formula_d,
        ).arrange(DOWN, buff=0.38)

        valores.to_edge(RIGHT, buff=0.7)
        valores.shift(0.25 * DOWN)

        texto_substituicao = Text(
            "Substituindo h e d:",
            color=BLACK,
            font_size=27,
        ).to_edge(LEFT, buff=0.8)
        texto_substituicao.shift(1.65 * UP)

        # ----------------------------------------------------
        # Passos da dedução
        # ----------------------------------------------------

        passo_1 = MathTex(
            r"V_{\text{tronco}}",
            r"=",
            r"\frac{1}{3}B"
            r"\left("
            r"\frac{k\sqrt{B}}{\sqrt{B}-\sqrt{b}}"
            r"\right)",
            r"-",
            r"\frac{1}{3}b"
            r"\left("
            r"\frac{k\sqrt{b}}{\sqrt{B}-\sqrt{b}}"
            r"\right)",
            color=BLACK,
            font_size=42,
        )

        passo_1[0].set_color(BLUE_E)
        passo_1[2].set_color(PURPLE)
        passo_1[4].set_color(ORANGE)

        passo_2 = MathTex(
            r"V_{\text{tronco}}",
            r"=",
            r"\frac{kB\sqrt{B}}"
            r"{3(\sqrt{B}-\sqrt{b})}",
            r"-",
            r"\frac{kb\sqrt{b}}"
            r"{3(\sqrt{B}-\sqrt{b})}",
            color=BLACK,
            font_size=47,
        )

        passo_2[0].set_color(BLUE_E)
        passo_2[2].set_color(PURPLE)
        passo_2[4].set_color(ORANGE)

        passo_3 = MathTex(
            r"V_{\text{tronco}}",
            r"=",
            r"\frac{k\left(B\sqrt{B}-b\sqrt{b}\right)}"
            r"{3(\sqrt{B}-\sqrt{b})}",
            color=BLACK,
            font_size=48,
        )

        passo_3[0].set_color(BLUE_E)
        passo_3[2].set_color(BLACK)

        observacao = Text(
            "Agora usamos uma fatoração de diferença de cubos.",
            color=BLACK,
            font_size=25,
        ).to_edge(DOWN, buff=0.55)

        equivalencia = MathTex(
            r"B\sqrt{B}",
            r"=",
            r"(\sqrt{B})^3",
            r"\qquad",
            r"b\sqrt{b}",
            r"=",
            r"(\sqrt{b})^3",
            color=BLACK,
            font_size=43,
        ).shift(1.55 * DOWN)

        equivalencia[0].set_color(BLUE_E)
        equivalencia[2].set_color(BLUE_E)
        equivalencia[4].set_color(GREEN_D)
        equivalencia[6].set_color(GREEN_D)

        diferenca_cubos = MathTex(
            r"x^3-y^3",
            r"=",
            r"(x-y)(x^2+xy+y^2)",
            color=BLACK,
            font_size=47,
        ).shift(1.55 * DOWN)

        fatoracao = MathTex(
            r"B\sqrt{B}-b\sqrt{b}",
            r"=",
            r"(\sqrt{B}-\sqrt{b})"
            r"\left(B+\sqrt{Bb}+b\right)",
            color=BLACK,
            font_size=43,
        ).shift(1.55 * DOWN)

        fatoracao[0].set_color(BLACK)
        fatoracao[2].set_color(BLACK)

        passo_4 = MathTex(
            r"V_{\text{tronco}}",
            r"=",
            r"\frac{k(\sqrt{B}-\sqrt{b})"
            r"\left(B+\sqrt{Bb}+b\right)}"
            r"{3(\sqrt{B}-\sqrt{b})}",
            color=BLACK,
            font_size=43,
        )

        passo_4[0].set_color(BLUE_E)

        # Cancelamento explícito
        passo_5 = MathTex(
            r"V_{\text{tronco}}",
            r"=",
            r"\frac{k}{3}",
            r"\left(B+\sqrt{Bb}+b\right)",
            color=BLACK,
            font_size=55,
        )

        passo_5[0].set_color(BLUE_E)
        passo_5[2].set_color(RED)
        passo_5[3].set_color(BLACK)

        resultado_final = MathTex(
            r"V_{\text{tronco}}",
            r"=",
            r"\frac{k}{3}",
            r"\left(B+b+\sqrt{Bb}\right)",
            color=BLACK,
            font_size=60,
        )

        resultado_final[0].set_color(BLUE_E)
        resultado_final[2].set_color(RED)

        significado = VGroup(
            MathTex(
                r"B",
                r"=",
                r"\text{área da base maior}",
                color=BLACK,
                font_size=32,
            ),
            MathTex(
                r"b",
                r"=",
                r"\text{área da base menor}",
                color=BLACK,
                font_size=32,
            ),
            MathTex(
                r"k",
                r"=",
                r"\text{altura do tronco}",
                color=BLACK,
                font_size=32,
            ),
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.25,
        )

        significado[0][0].set_color(BLUE_E)
        significado[1][0].set_color(GREEN_D)
        significado[2][0].set_color(RED)

        significado.next_to(resultado_final, DOWN, buff=0.55)

        # ----------------------------------------------------
        # Animação
        # ----------------------------------------------------

        self.play(Write(titulo))
        self.play(FadeIn(subtitulo, shift=0.15 * UP))

        self.play(
            Write(ideia),
            run_time=1.7,
        )

        self.wait(1)

        self.play(
            TransformMatchingTex(
                ideia,
                volumes,
            ),
            run_time=1.6,
        )

        self.wait(1)

        # Desloca a fórmula para a esquerda
        self.play(
            volumes.animate.to_edge(LEFT, buff=0.7).shift(0.2 * UP),
            FadeIn(valores, shift=0.2 * LEFT),
            run_time=1.4,
        )

        self.play(Write(texto_substituicao))
        self.wait(1)

        self.play(
            FadeOut(volumes),
            FadeOut(valores),
            FadeOut(texto_substituicao),
        )

        self.play(
            Write(passo_1),
            run_time=2,
        )

        self.wait(1)

        self.play(
            TransformMatchingTex(
                passo_1,
                passo_2,
            ),
            run_time=1.7,
        )

        self.wait(0.8)

        self.play(
            TransformMatchingTex(
                passo_2,
                passo_3,
            ),
            run_time=1.7,
        )

        self.wait(1)

        # Explicação da diferença de cubos
        self.play(
            passo_3.animate.shift(1.05 * UP),
            FadeIn(observacao),
        )

        self.play(
            Write(equivalencia),
            run_time=1.7,
        )

        self.wait(1)

        self.play(
            TransformMatchingTex(
                equivalencia,
                diferenca_cubos,
            ),
            run_time=1.5,
        )

        self.wait(1)

        self.play(
            TransformMatchingTex(
                diferenca_cubos,
                fatoracao,
            ),
            run_time=1.7,
        )

        self.wait(2)

        self.play(
            FadeOut(observacao),
            FadeOut(fatoracao),
        )

        self.play(
            TransformMatchingTex(
                passo_3,
                passo_4,
            ),
            run_time=2,
        )

        self.wait(1)

        # Destaca os fatores que serão cancelados
        cancelamento = Text(
            "Cancelamos o fator comum",
            color=BLACK,
            font_size=27,
        ).to_edge(DOWN, buff=0.6)

        self.play(Write(cancelamento))

        self.play(
            Circumscribe(
                passo_4,
                color=YELLOW_D,
                buff=0.18,
            ),
            run_time=1.4,
        )

        self.play(
            TransformMatchingTex(
                passo_4,
                passo_5,
            ),
            FadeOut(cancelamento),
            run_time=1.8,
        )

        self.wait(1)

        self.play(
            TransformMatchingTex(
                passo_5,
                resultado_final,
            ),
            run_time=1.5,
        )

        caixa = SurroundingRectangle(
            resultado_final,
            color=BLUE_E,
            buff=0.25,
            stroke_width=4,
        )

        self.play(Create(caixa))
        self.play(FadeIn(significado, shift=0.15 * UP))

        self.wait(4)

        self.play(
            FadeOut(
                VGroup(
                    titulo,
                    subtitulo,
                    resultado_final,
                    caixa,
                    significado,
                )
            )
        )

# ============================================================
# VÍDEO COMPLETO — VOLUME DO TRONCO DE PIRÂMIDE
# ============================================================

class VideoCompletoTronco(ThreeDScene):
    def preparar_proxima_cena(self):
        """
        Limpa os objetos da cena anterior e devolve a câmera
        para a posição frontal padrão.
        """
        self.stop_ambient_camera_rotation()

        self.clear()

        self.set_camera_orientation(
            phi=0 * DEGREES,
            theta=-90 * DEGREES,
            gamma=0 * DEGREES,
            zoom=1,
            frame_center=ORIGIN,
        )

        self.wait(0.3)

    def construct(self):
        # ----------------------------------------------------
        # Cena 1 — Introdução
        # ----------------------------------------------------
        self.next_section(
            name="Introdução",
            skip_animations=False,
        )

        Introducao.construct(self)

        self.preparar_proxima_cena()

        # ----------------------------------------------------
        # Cena 2 — Formação do tronco
        # ----------------------------------------------------
        self.next_section(
            name="Formação do tronco",
            skip_animations=False,
        )

        FormacaoDoTronco.construct(self)

        self.preparar_proxima_cena()

        # ----------------------------------------------------
        # Cena 3 — Separação da pirâmide
        # ----------------------------------------------------
        self.next_section(
            name="Separação da pirâmide",
            skip_animations=False,
        )

        SeparacaoDoTronco.construct(self)

        self.preparar_proxima_cena()

        # ----------------------------------------------------
        # Cena 4 — Identificação das medidas
        # ----------------------------------------------------
        self.next_section(
            name="Identificação das medidas",
            skip_animations=False,
        )

        IdentificacaoDasMedidas.construct(self)

        self.preparar_proxima_cena()

        # ----------------------------------------------------
        # Cena 5 — Semelhança das pirâmides
        # ----------------------------------------------------
        self.next_section(
            name="Semelhança das pirâmides",
            skip_animations=False,
        )

        SemelhancaDasPiramides.construct(self)

        self.preparar_proxima_cena()

        # ----------------------------------------------------
        # Cena 6 — Dedução das alturas
        # ----------------------------------------------------
        self.next_section(
            name="Dedução das alturas",
            skip_animations=False,
        )

        DeducaoDasAlturas.construct(self)

        self.preparar_proxima_cena()

        # ----------------------------------------------------
        # Cena 7 — Fórmula final
        # ----------------------------------------------------
        self.next_section(
            name="Fórmula final",
            skip_animations=False,
        )

        FormulaVolumeDoTronco.construct(self)