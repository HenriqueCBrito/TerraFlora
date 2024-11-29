const peso = Math.floor(Math.random() * (1000 - 100 + 1)) + 100;
describe('Calculador de Plantio ', () => {
  
  before(() => {
    cy.exec('python ./create_superuser.py');
    cy.visit('/');
    cy.contains('Cadastro').click();
    cy.get('input[name="email"]').type('teste@teste.com');
    cy.get('input[name="username"]').type('usuarioTeste');
    cy.get('input[name="full_Name"]').type('Jorginho Silva');
    cy.get('input[name="cpf"]').type('12345678901');
    cy.get('input[name="phone_number"]').type('+5581912345678');
    cy.get('input[name="street"]').type('Cais do Apolo');
    cy.get('input[name="home_number"]').type('123');
    cy.get('input[name="city"]').type('Recife');
    cy.get('input[name="state"]').type('PE');
    cy.get('input[name="country"]').type('Brasil');
    cy.get('input[name="password"]').type('senha123');
    cy.get('input[name="confirm_password"]').type('senha123');
    cy.get('button[type="submit"]').click();
    cy.contains('FAZENDAS').click({ force: true });
    cy.contains("REGISTRAR FAZENDA").click({ force: true });
    cy.get('#farm_name').type('Fazenda TerraFlora', { force: true });
    cy.get('#street').type('Rua das Palmeiras', { force: true });
    cy.get('#home_number').type('123', { force: true });
    cy.get('#city').type('Recife', { force: true });
    cy.get('#state').type('PE', { force: true });
    cy.get('#country').type('Brasil', { force: true });
    cy.get('#size').type('100', { force: true });
    cy.get('#size_unit').select('ha', { force: true });
    cy.get('button[type="submit"]').click({ force: true });
    cy.contains("Home").click({ force: true });
  });

  it('Selecionando fazenda e gerando lista de compras', () => {
    cy.contains('CULTURAS').click({ force: true });
    cy.contains("Registrar Nova Cultura").click({ force: true });
    cy.get('#name').type('Tomate');
    cy.get('#crop_type').select('vegetable');
    cy.get('#planting_season').type('Primavera');
    cy.get('#harvest_season').type('Verão');
    cy.get('#growing_conditions').type('Solo bem drenado, clima quente');
    cy.get('#compatible_plants').type('Alface, Manjericão');
    cy.get('#common_pests').type('Pulgões, ácaros');
    cy.get('#watering_needs').type('Moderada');
    cy.get('#sun_exposure').type('Pleno sol');
    cy.get('#notes').type('Prefere solos férteis e bem irrigados');
    cy.get('button[type="submit"]').click();
    cy.get('#desired_harvest').type(peso);
    cy.get('button[type="button"]').click();
  });

  after(() => {
    cy.visit('/admin/', { force: true });
    cy.get('#id_username').type('admin@admin.com', { force: true });
    cy.get('#id_password').type('admin123', { force: true });
    cy.get('.submit-row > input').click({ force: true });
    cy.contains('Users').click({ force: true });
    cy.get('#searchbar').type('teste@teste.com', { force: true });
    cy.get('#changelist-search > div > [type="submit"]').click({ force: true });
    cy.contains('teste@teste.com').should('be.visible', { force: true });
    cy.get('.action-select').click({ force: true });
    cy.get('select').select('Delete selected users', { force: true });
    cy.get('.button').click({ force: true });
    cy.get('div > [type="submit"]').click({ force: true });
  });
  
});