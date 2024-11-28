describe('Calculadora de Plantio', () => {
  
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
    cy.contains('ARMAZENAMENTO').click({ force: true });
    cy.contains("Lista de Compras").click({ force: true });
    cy.get('#farm_id').select('Fazenda TerraFlora', { force: true });
    const budget = Math.floor(Math.random() * 701); 
    cy.get('#budget').type(budget.toString(), { force: true });
    cy.get('button[type="submit"]').click({ force: true });
  });

  after(() => {
    cy.visit('/admin/');
    cy.get('#id_username').type('admin@admin.com');
    cy.get('#id_password').type('admin123');
    cy.get('.submit-row > input').click();
    cy.contains('Users').click();
    cy.get('#searchbar').type('teste@teste.com');
    cy.get('#changelist-search > div > [type="submit"]').click();
    cy.contains('teste@teste.com').should('be.visible');
    cy.get('.action-select').click();
    cy.get('select').select('Delete selected users');
    cy.get('.button').click();
    cy.get('div > [type="submit"]').click();
  });
});
