
#version 330 core
layout (triangles) in;
layout (triangle_strip, max_vertices = 3) out;

in VS_OUT {
    vec2 texCoords;
	vec3 fragPos;
    vec3 normal;
} gs_in[];

out vec2 TexCoords;
out vec3 Normal;
out vec3 FragPos;

vec4 explode(vec4 position, vec3 normal)
{
    return position ;
}

vec3 GetNormal()
{
    vec3 a = vec3(gl_in[0].gl_Position) - vec3(gl_in[1].gl_Position);
    vec3 b = vec3(gl_in[2].gl_Position) - vec3(gl_in[1].gl_Position);
    return normalize(cross(a, b));
}

void main() {
    vec3 normal = GetNormal();

    gl_Position = explode(gl_in[0].gl_Position, normal);
    FragPos = gl_Position.xyz;
    Normal = normal;
    TexCoords = gs_in[0].texCoords;
    EmitVertex();


    gl_Position = explode(gl_in[1].gl_Position, normal);
    Normal =normal;
    FragPos = gl_Position.xyz;
    TexCoords = gs_in[1].texCoords;
    EmitVertex();

    gl_Position = explode(gl_in[2].gl_Position, normal);
    Normal = normal;
    FragPos = gl_Position.xyz;
    TexCoords = gs_in[2].texCoords;
    EmitVertex();

    EndPrimitive();
}
